from django.shortcuts import render
from .models import announcement


def index(request):
    return render(request, 'main/index.html')


def basket(request):
    return render(request, 'main/basket.html')


def take(request):
    return render(request, 'main/take.html')


def getby(request):
    return render(request, 'main/getby.html')


def category(request):
    return render(request, 'main/category.html')

def sport(request):
    return render(request, 'main/sport.html')


def child(request):
    return render(request, 'main/child.html')


def cloth(request):
    return render(request, 'main/cloth.html')


def other(request):
    return render(request, 'main/other.html')


def rest(request):
    return render(request, 'main/rest.html')



def catalog(request):
    tasks = announcement.objects.all()
    return render(request, 'main/catalog.html', {'tasks': tasks})
