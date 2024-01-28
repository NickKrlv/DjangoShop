from django.core.cache import cache
from config.settings import CACHE_ENABLED
from products.models import Product


def get_cached_products():
    if CACHE_ENABLED:
        products = cache.get('products')
        if products is None:
            products = Product.objects.all()
            cache.set('products', products, 60)
        return products
    else:
        return Product.objects.all()
