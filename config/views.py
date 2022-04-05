from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from store.models import Product

# Create your views here.


class HomeView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        products = Product.objects.all().filter(
            is_available=True).order_by('created_date')

        context = {
            'products': products,
        }

        return render(request, self.template_name, context)
