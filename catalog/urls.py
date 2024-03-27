from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactsView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name



urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

]
