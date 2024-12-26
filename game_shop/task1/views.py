from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game, News


# Create your views here.



def sign_up_by_html(request):
    buyers = Buyer.objects.all()
    users = [buyer.name for buyer in buyers]
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        # for buyer in buyers:
        if password == repeat_password and int(age) >= 18 and username not in users:
            Buyer.objects.create(name=username,balance= 1000, age=int(age))
            return HttpResponse(f"Приветствуем, {username}!")
        if username in users:
            info.update({'error': 'Пользователь уже существует'})
        if password != repeat_password:
                info.update({'error': 'Пароли не совпадают'})
        if int(age) < 18:
                info.update({'error': 'Вы должны быть старше 18'})

    return render(request, 'first_task/registration_page.html', context={'info': info,})






def sign_up_by_django(request):
    buyers = Buyer.objects.all()
    users = [buyer.name for buyer in buyers]
    info = {}
    form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and username not in users:
                Buyer.objects.create(name=username,balance= 1000, age=int(age))
                return HttpResponse(f"Приветствуем, {username}!")
            if password != repeat_password:
                info.update({'error': 'Пароли не совпадают'})
            if int(age) < 18:
                info.update({'error': 'Вы должны быть старше 18'})
            if username in users:
                info.update({'error': 'Пользователь уже существует'})

    else:
        form = UserRegister()
    return render(request, 'first_task/registration_page.html', context={'info': info,})


def home(requests):
    title = 'Магазин компьютерных игр"'
    text = 'Главная страница'

    context = {
        'title': title,
        'text': text,
    }
    return render(requests, 'first_task/platform.html', context)


def shop(requests):
    games = Game.objects.all()
    return render(requests, 'first_task/games.html', context={'games': games})


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


def news(requests):
    news_List = News.objects.all()
    paginator = Paginator(news_List,3)
    page_number = requests.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(requests, 'first_task/news.html', context = {'news':page_obj})