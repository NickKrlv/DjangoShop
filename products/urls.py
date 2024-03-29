from django.urls import path
from django.views.decorators.cache import cache_page

import products.views
from products.apps import ProductsConfig

app_name = 'products'
urlpatterns = [
    path('', products.views.ProductListView.as_view(), name='list'),
    path('view/<int:pk>/', cache_page(60)(products.views.ProductDetailView.as_view()), name='view'),
    path('create/', products.views.ProductCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', products.views.ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', products.views.ProductDeleteView.as_view(), name='delete')
]
