from django.forms import ModelForm
from django import forms
from .models import Food, Order


class OrderForm(ModelForm):
  class Meta:
    model = Order
    exclude = ['user', 'date',]

class FoodForm(ModelForm):
  class Meta:
    model = Food
    exclude = ['user']
