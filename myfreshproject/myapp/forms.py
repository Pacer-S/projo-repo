from dataclasses import fields
from tkinter import Image
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Product
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'description', 'price', 'image')