from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock',
                    'category', 'is_available')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_date', 'modified_date')


admin.site.register(Product, ProductAdmin)
