from django import forms
from products.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        if cleaned_data in ['casino', 'cripta', 'police', 'radar']:
            raise forms.ValidationError("You can't add such products")
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for dirty_word in ['fuck', 'sex', 'bustard']:
            if dirty_word in cleaned_data:
                raise forms.ValidationError(f"You can't add a description with such words: {dirty_word}")
        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
