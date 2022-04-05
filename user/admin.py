from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name',
                    'last_name', 'phone_number', 'password', 'date_joined', 'last_login')
    list_display_links = ('email', 'username', )
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
         'fields': ('first_name', 'last_name', 'phone_number')}),
        ('dates', {'fields': ('date_joined', 'last_login')}),
        ('Permissions', {'fields': ('is_admin',
         'is_staff', 'is_superadmin', 'is_activ')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
