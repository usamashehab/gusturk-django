from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from category.models import Category
from store.models import Product
from django.views.generic.detail import DetailView

# Create your views here.


class StoreView(View):
    template_name = 'store/home.html'

    def get(self, request, * args, **kwargs):
        category = None
        category = kwargs.get('category_slug', None)

        if category != None:
            category = get_object_or_404(
                Category, slug=kwargs['category_slug'])
            products = category.products.all().filter(
                is_available=True).order_by('created_date')
        else:
            products = Product.objects.all().filter(
                is_available=True).order_by('created_date')
        context = {
            'products': products,
        }
        return render(request, self.template_name, context)


class ProductDetail(DetailView):
    model = Product
    template_name = 'store/product.html'
