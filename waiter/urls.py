from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.views.generic import ListView
from waiter.models import Food,Order
from django.conf.urls import url, include
from waiter.views import restaurant,vote
from django.views.generic.base import TemplateView

urlpatterns = [
   url(r'^$',
       ListView.as_view(model=Food,
       template_name='restaurants/index.html'),
       name='index'),
   url(r'^rest/(\d+)/$',
       restaurant,
       name='restaurant'),
   url(r'^(\d+)/vote/$',
       vote,
       name='vote'),
   url(r'^eastland', TemplateView.as_view(template_name='restaurants/Eastland/eastland.html'), name='eastland'),
   # url(r'^emenu', TemplateView.as_view(template_name='restaurants/Eastland/emenu.html'), name='emenu'),
   url(r'^grand', TemplateView.as_view(template_name='restaurants/Grand/grand.html'), name='grand'),
   # url(r'^gmenu', TemplateView.as_view(template_name='restaurants/Grand/gmenu.html'), name='gmenu'),
   url(r'^jumuia', TemplateView.as_view(template_name='restaurants/Jumuia/jumuia.html'), name='jumuia'),
   # url(r'^jmenu', TemplateView.as_view(template_name='restaurants/Jumuia/jmenu.html'), name='jmenu'),
   url(r'^kempinski', TemplateView.as_view(template_name='restaurants/Kempinski/kempinski.html'), name='kempinski'),
   # url(r'^kmenu', ListView.as_view(model=Food,template_name='restaurants/Kempinski/kmenu.html'), name='kmenu'),
   url(r'^menu/(?P<restaurant>\w+)$',views.food_list, name='menu'),
   url(r'^kmenu/',views.food_list, name='kmenu'),
   url(r'^menu/',views.food_list, name='menu'),
    url(r'^jmenu/',views.food_list, name='jmenu'),
    url(r'^gmenu/',views.food_list, name='gmenu'),
    url(r'^emenu/',views.food_list, name='emenu'),

    url(r'^order/',views.order_list, name='order'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
