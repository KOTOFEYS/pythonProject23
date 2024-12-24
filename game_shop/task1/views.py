from django.shortcuts import render
from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from .form import UserRegister
from .models import Buyer, Game
# Create your views here.

def sign_up_by_html(request):
    buyers = Buyer.objects.all()
    info = {}

    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        for name in buyers:
            if password == repeat_password and int(age) >= 18 and name not in buyers:
                Buyer.object.create(name='name', age=int(age))
                return HttpResponse(f"Приветствуем, {name}!")
        if password != repeat_password:
            info.update({'error': 'Пароли не совпадают'})
        if int(age) < 18:
            info.update({'error': 'Вы должны быть старше 18'})
        if name in buyers:
            info.update({'error': 'Пользователь уже существует'})
    return render(request, 'first_task/registration_page.html', context={'info': info,})

def sign_up_by_django(request):
    buyers = Buyer.objects.all()
    info = {}
    # form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and name not in buyers:
                Buyer.object.create(name='name', age='age')
                return HttpResponse(f"Приветствуем, {name}!")
            if password != repeat_password:
                info.update({'ERROR1': 'Пароли не совпадают'})
            if int(age) < 18:
                info.update({'ERROR2': 'Вы должны быть старше 18'})
            if name in buyers:
                info.update({'ERROR3': 'Пользователь уже существует'})
        else:
            form = UserRegister()
    return render(request, 'first_task/registration_page.html', context={'info': info, })

# Create your views here.
def home(requests):
    title = 'Детский магазин "МЕДВЕЖЁНОК"'
    text = 'Главная страница'

    context = {
        'title': title,
        'text': text,
    }
    return render(requests, 'first_task/platform.html', context)


def shop(requests):
    title = 'Детские товары'
    text = 'Детские товары'
    list_shop = ['Велосипед', 'Кукла', 'Конструктор']
    context = {
        'title': title,
        'text': text,
        'list_shop': list_shop
    }
    return render(requests, 'first_task/games.html', context)


def basket(requests):
    title = 'Корзина'
    text = 'Корзина'
    text1 = 'Извините, ваша корзина пуста'

    context = {
        'title': title,
        'text': text,
        'text1': text1
    }
    return render(requests, 'first_task/cart.html', context)
# def parent(requests):
#     return render(requests, 'first_task/menu.html')