from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    # category name can't be repeated so it's unique
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        #  django always add just 's' after names so we have to tell
        # it the correct plural name
        verbose_name = "category"
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        # note --> args here is list [, , ,...]
        return reverse('store:category', args=[self.slug])

    def __str__(self):
        return self.name
