from django.contrib import admin

from users.models import User
from .models import Product, Version, Category
from blog.models import BlogPost


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category', 'date_create', 'owner')
    list_filter = ('category', 'date_create', 'owner')
    search_fields = ['name', 'description']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ['name', 'description']


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'number_version', 'name_version', 'active_version')
    list_filter = ('product', 'active_version')
    search_fields = ['product', 'name_version']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'content', 'date_created', 'is_published')
    list_filter = ('date_created', 'is_published')
    search_fields = ['title', 'content']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', )
    search_fields = ['username', 'email']
