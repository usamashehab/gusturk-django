from unicodedata import name
from django.urls import path
from . import views
app_name = 'store'
urlpatterns = [
    path('', views.StoreView.as_view(), name='home'),
    path('category/<slug:category_slug>/',
         views.StoreView.as_view(), name='category'),
    path('category/<slug:category_slug>/<slug:slug>/',
         views.ProductDetail.as_view(), name='product')
]
