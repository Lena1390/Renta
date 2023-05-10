from django.shortcuts import render
from .models import announcement


def index(request):
    return render(request, 'main/index.html')


def basket(request):
    return render(request, 'main/basket.html')


def take(request):
    return render(request, 'main/take.html')


def category(request):
    return render(request, 'main/category.html')


def catalog(request):
    tasks = announcement.objects.all()
    return render(request, 'main/catalog.html', {'tasks': tasks})
