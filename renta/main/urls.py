from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='home'),
        path('basket', views.basket, name='basket'),
        path('catalog', views.catalog, name='catalog'),
        path('take', views.take, name='take'),
        path('getby', views.getby, name='getby'),
        path('category', views.category, name='category'),
        path('sport', views.sport, name='sport'),
        path('child', views.child, name='child'),
        path('cloth', views.cloth, name='cloth'),
        path('other', views.other, name='other'),
        path('rest', views.rest, name='rest'),

]