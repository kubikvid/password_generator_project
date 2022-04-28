from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password': '123456'})

def eggs(request):
    return HttpResponse('Хорошие яйца, бро')