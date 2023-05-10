from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='home'),
        path('basket', views.basket, name='basket'),
        path('catalog', views.catalog, name='catalog'),
        path('take', views.take, name='take'),
        path('category', views.category, name='category')
]