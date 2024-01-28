from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.http import Http404
from django.contrib import messages

from config.settings import CACHE_ENABLED
from products.models import Product, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from products.forms import ProductForm, VersionForm
from django.forms import inlineformset_factory, modelform_factory

from products.services import get_cached_products


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['products'] = get_cached_products()
        return context_data


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:list')
    permission_required = 'products.add_product'

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:list')
    permission_required = 'products.change_product'

    def get_form_class(self):
        fields = []
        if self.request.user.has_perm('products.set_product_active'):
            fields.append('is_active')
        if self.request.user.has_perm('products.set_category'):
            fields.append('category')
        if self.request.user.has_perm('products.set_description'):
            fields.append('description')
        if len(fields) > 0:
            return modelform_factory(form=ProductForm, model=Product, fields=fields)
        return ProductForm

    def test_func(self):
        self.object = super().get_object()
        if (self.request.user.has_perm('products.change_product')
                and (self.object.created_by == self.request.user
                     or self.request.user.has_perm('products.set_product_active')
                     or self.request.user.has_perm('products.set_category')
                     or self.request.user.has_perm('products.set_description'))):
            return True
        return False

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        messages.success(self.request, 'Product updated successfully')
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('products:list')
    permission_required = 'products.delete_product'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)

        if not obj.owner == self.request.user and not self.request.user.is_superuser:
            raise Http404("You do not have permission to access this page")

        return obj
