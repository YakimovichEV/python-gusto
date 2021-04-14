from django import forms
from django.db import models
from .models import UsersMessages, Dish, Category
import os
from uuid import uuid4


class UserMessageForm(forms.ModelForm):
    user_name = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'type': 'text', 'id': 'name', 'class': 'form-control',
                                                              'placeholder': 'Ім\'я', 'required': 'required'}))
    user_email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email', 'id': 'email',
                                                                'class': 'form-control',
                                                                'placeholder': 'Електронна пошта',
                                                                'required': 'required'}))
    message = forms.CharField(max_length=200,
                              widget=forms.Textarea(
                                  attrs={'name': 'message', 'id': 'message', 'class': 'form-control',
                                         'rows': '4', 'placeholder': 'Повідомлення',
                                         'required': 'required'}))

    class Meta:
        model = UsersMessages
        fields = ('user_name', 'user_email', 'message')


class CategoryAddForm(forms.ModelForm):
    title = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'type': 'text', 'id': 'title',
                                                                        'class': 'form-control',
                                                                        'placeholder': 'Назва категорії',
                                                                        'required': 'required'}))
    is_visible = forms.BooleanField(initial=True, required=False)
    is_special = forms.BooleanField(initial=True, required=False)
    category_order = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'number', 'id': 'category_order',
                                                                        'class': 'form-control',
                                                                        'placeholder': 'Порядок категорії',
                                                                        'required': 'required'}))

    class Meta:
        model = Category
        fields = ('title', 'category_order', 'is_visible', 'is_special')


class DishAddForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type': 'text', 'id': 'title',
                                                                         'class': 'form-control',
                                                                         'placeholder': 'Назва блюда',
                                                                         'required': 'required'}))
    price = forms.DecimalField(max_digits=7, decimal_places=2, widget=forms.TextInput(attrs={'type': 'number', 'id': 'price',
                                                                        'class': 'form-control',
                                                                        'placeholder': 'Ціна',
                                                                        'required': 'required'}))
    is_visible = forms.BooleanField(initial=True, required=False)
    description = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'type': 'text', 'id': 'description',
                                                                         'class': 'form-control',
                                                                         'placeholder': 'Опис',
                                                                         'required': 'required'}))
    photo = forms.ImageField(widget=forms.FileInput)
    category = forms.Select()
    weight = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'number', 'id': 'weight',
                                                                        'class': 'form-control',
                                                                        'placeholder': 'Вага',
                                                                        'required': 'required'}))

    class Meta:
        model = Dish
        fields = ('title', 'price', 'is_visible', 'description', 'photo', 'category', 'weight')
