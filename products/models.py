from django.db import models
from datetime import datetime
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    description = models.TextField(**NULLABLE, verbose_name='description')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    description = models.TextField(verbose_name='description')
    image = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, **NULLABLE, verbose_name='category')
    price = models.IntegerField(verbose_name='price')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='date_create')
    change_data = models.DateTimeField(auto_now=True, **NULLABLE, verbose_name='change_data')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='owner', **NULLABLE)
    is_active = models.BooleanField(verbose_name='is_active', default=True)

    def __str__(self):
        return f"{self.name} {self.price}"

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        permissions = [
            ('set_product_active', 'Can set product active'),
            ('set_category', 'Can set category'),
            ('set_description', 'Can set description'),
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product')
    number_version = models.CharField(max_length=10, verbose_name='number_version')
    name_version = models.CharField(max_length=30, verbose_name='name_version')
    active_version = models.BooleanField(verbose_name='actual_version', default=True)

    def __str__(self):
        return f"{self.product} - {self.name_version} - {self.active_version}"

    class Meta:
        verbose_name = 'version'
        verbose_name_plural = 'versions'
