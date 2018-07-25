from django.db import models
from django import forms
from datetime import date

class Restaurant(models.Model):
    name=models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    # description = models.TextField(blank=True, null=True)
    price = models.DecimalField('Shs amount', max_digits=8, decimal_places=2, blank=True, null=True)
    date = models.DateField(default=date.today)
    BOOL_CHOICES = (('Available', 'Available'), ('Unavailable', 'Unavailable'))
    availability = models.CharField(max_length=50,choices=BOOL_CHOICES, default='Unavailable')
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,blank=True,null=True)


    def __str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=30)
    food_name = models.CharField(max_length=30)
    table_number = models.CharField(max_length=40)
    quantity = models.IntegerField(null=True)
    date = models.DateField(default=date.today)
    BOOL_CHOICES = ((True, 'Plate'), (False, 'Takeaway'))

    mode = models.NullBooleanField(choices=BOOL_CHOICES)

    def __str__(self):
        return self.name
