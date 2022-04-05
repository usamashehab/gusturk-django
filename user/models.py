from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, phone_number, email, password=None):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("user must have an email address")
        if not username:
            raise ValueError("user must have a username")
        if not password:
            raise ValueError("user must have a password")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, phone_number, email, password):
        # creating normal user then give him permissions
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,

        )
        user.is_admin = True
        user.is_activ = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)

    #  required fields
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_activ = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    class Meta:
        #  django always add just 's' after names so we have to tell
        # it the correct plural name
        verbose_name = "user"
        verbose_name_plural = "users"

    USERNAME_FIELD = 'email'
    # note that REQUIRED_FIELDS is plural-->'FIELDS'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number']

    objects = CustomUserManager()  # still don't know what is objects exactly

    # methods
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def short_name(self):
        return f"{self.first_name} "

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
