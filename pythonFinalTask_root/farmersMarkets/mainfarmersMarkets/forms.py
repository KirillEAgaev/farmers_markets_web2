from .models import Category
from django.forms import ModelForm, TextInput


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category']
        widgets = {"category": TextInput(attrs={
            'class':'form-control',
            'placeholder':'Введите название'
        })
        }