from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz') #создаем список символов из строки

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) #добавляем к списку заглавные символы

    if request.GET.get('special'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) #добавляем к списку заглавные символы


    length = int(request.GET.get('length', 12))# Получаем параметры из строки запроса
    the_password = ''
    for x in range(length):
        the_password += random.choice(characters) #Выбират случайные буквы
    return render(request, 'generator/password.html', {'password': the_password})