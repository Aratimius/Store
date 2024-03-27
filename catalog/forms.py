from django import forms
from django.forms import BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


    def clean_sample(self, model_attribute: str, attribute_name: str):
        """Метод для избежания дублирования кода в clean_.."""
        cleaned_data = self.cleaned_data[model_attribute]
        forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция",
                           "радар"]
        if cleaned_data.lower() in forbidden_words:
            raise forms.ValidationError(f'В {attribute_name} присудствуют запрещенные слова!')
        return cleaned_data

    def clean_name(self):
        """Проверка названия товара"""
        cleaned_data = self.clean_sample('name', 'названии')
        return cleaned_data

    def clean_description(self):
        """Проверка описания товара"""
        cleaned_data = self.clean_sample('description', 'описании')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

