from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def info(request):
    return render(request, 'generator/info.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz') #создаем список символов из строки

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) #добавляем к списку заглавные символы

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()-_+=;:,./?\|`~[]{}')) #добавляем к списку специальные символы

    if request.GET.get('numbers'):
        characters.extend(list('0123456789')) #добавляем к списку цифры


    length = int(request.GET.get('length', 12))# Получаем параметры из строки запроса
    the_password = ''
    for x in range(length):
        the_password += random.choice(characters) #Выбират случайные символы
    return render(request, 'generator/password.html', {'password': the_password})