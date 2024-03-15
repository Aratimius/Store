from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, TemplateView, CreateView

from catalog.models import Product, Category


class ContactsView(TemplateView):
    """Недописан"""
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты',
        'description': 'Заполните форму, и мы с вами свяжемся'
    }

    def post(self, request):
        """в TemplateView есть только метод get, поэтому post прописан вручную"""
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
        return render(request, self.template_name)


class HomeListView(ListView):
    """Для главной страницы"""
    model = Product
    extra_context = {
        'title': 'Store',
        'description': 'Это магазин разных товаров',
    }


class ProductDetailView(DetailView):
    """Для подробного описания товара"""
    model = Product


# FBV------------------------------------------------------------------------------------------------------------------
# def contacts(request):
#     context = {
#         'title': 'Контакты',
#         'description': 'Заполните форму, и мы с вами свяжемся'
#     }
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'{name} ({phone}): {message}')
#
#     return render(request, 'catalog/contacts.html', context)


# def home(request):
#     context = {
#         'product_list': Product.objects.all(),
#         'title': 'Store',
#         'description': 'Это магазин разных товаров'
#     }
#
#     return render(request, 'catalog/home.html', context)


# def product_details(request, pk):
#     context = {
#         'product': Product.objects.get(pk=pk),
#         'title': 'Подробное описание товара',
#         'description': 'Все, что вам нужно знать о товаре'
#     }
#     return render(request, 'catalog/details.html', context)
