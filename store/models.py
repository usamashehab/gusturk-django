from distutils.command.upload import upload
from django.db import models
from django.urls import reverse
from django.utils import timezone
from category.models import Category

# Create your models here.


class Product(models.Model):
    name = models.CharField(
        max_length=250, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length=250)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products', null=True)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("store:product", args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name
