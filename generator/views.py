# coding: utf-8
from random import choice

from django.http import HttpResponse
from django.shortcuts import render


LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = LOWERCASE_LETTERS.upper()
NUMBERS = ''.join(str(n) for n in range(10))
SPECIAL_CHARACTERS = '!@#$%^&*()-_+=;:,./?\|`~[]{}'


def home(request):
    return render(request, 'generator/home.html')


def info(request):
    return render(request, 'generator/info.html')


def password_view(request):

    characters = list(LOWERCASE_LETTERS) # создаем список символов из строки

    if request.GET.get('uppercase'):
        characters.extend(UPPERCASE_LETTERS) # добавляем к списку заглавные символы

    if request.GET.get('special'):
        characters.extend(SPECIAL_CHARACTERS) # добавляем к списку специальные символы

    if request.GET.get('numbers'):
        characters.extend(NUMBERS) # добавляем к списку цифры

    length = int(request.GET.get('length', 12)) # получаем параметры из строки запроса

    password = ''.join((choice(characters) for _ in range(length)))

    return render(request, 'generator/password.html', {'password': password})
