from django.contrib import admin
from django.contrib import admin
# from .models import Menu
from waiter.models import Food, Order,Restaurant
# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [('Description',{'fields': ['name','desc','menu']}),
                 ('Address',{'fields':['address','post_code','town']}),
                 ('Contact',{'fields':['web','gmap_url','phone']}),
                 ('Food',{'fields':['food']}),
                 ('Pictures',{'fields':['picture','map']}),]
admin.site.register(Food)
admin.site.register(Order)
admin.site.register(Restaurant)
