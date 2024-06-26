from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Category, Version


class ContactsView(LoginRequiredMixin, TemplateView):
    """Недописан"""

    template_name = "catalog/contacts.html"
    extra_context = {
        "title": "Контакты",
        "description": "Заполните форму, и мы с вами свяжемся",
    }

    def post(self, request):
        """в TemplateView есть только метод get, поэтому post прописан вручную"""
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")

        return render(request, self.template_name)


class ProductListView(LoginRequiredMixin, ListView):
    """Для главной страницы"""

    model = Product
    extra_context = {
        "title": "Store",
        "description": "Это магазин разных товаров",
    }


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Для подробного описания товара"""

    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        """Привязать пользователя к продукту"""
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1
        )
        if self.request.method == "POST":
            context_data["formset"] = VersionFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = VersionFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()["formset"]
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")


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
