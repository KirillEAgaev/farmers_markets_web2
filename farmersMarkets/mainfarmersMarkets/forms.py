from .models import Categories
from django.forms import ModelForm, TextInput


class CategoryForm(ModelForm):
    class Meta:
        model = Categories
        fields = ['category']
        widgets = {"category": TextInput(attrs={
            'class':'form-control',
            'placeholder':'Введите название'
        })
        }