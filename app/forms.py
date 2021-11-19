from django import forms
from django.forms import ModelForm
from .models import Item, Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateProductForm(forms.Form):
    class Meta:
        model = Item
        fields = '__all__'
        
    CATEGORIES = (
        ('Food', 'Food'),
        ('Electronics', 'Electronics'),
        ('Sports', 'Sports'),
        ('Health & Beauty', 'Health & Beauty'),
        ('Household', 'Household'),
        ('Appliances', 'Appliances'),
        ('Furniture', 'Furniture'),
        ('Outdoors', 'Outdoors'),
        ('Clothing', 'Clothing'),
        ('Misc.', 'Misc.')
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Product name...', 'style': 'width: 275px; color: red;'}), max_length=100, required=True)
    price = forms.FloatField(widget=forms.TextInput(attrs={'placeholder':'$....', 'style': 'width: 280px; color: red;'}), required=True)
    category = forms.CharField(label="What category is your item?", widget=forms.Select(choices=CATEGORIES,  attrs={'placeholder': 'Item Category', 'style': 'width: 330px; color: red;'}), required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ex: Kinda smelly, may or may not be broken', 'style': 'width: 330px; height: 50px; color:red;'}), max_length=300, required=True)
    img_link = forms.URLField(label="Image Link", widget=forms.TextInput(attrs={'placeholder':'Image not required', 'style': 'width: 330px; color: red;'}), required=False)