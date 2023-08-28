from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, get_object_or_404 # get_object_or_404 работает аналогично get,т.е.делает selectз апрос к базе данных.Но если запрос не вернёт строку из таблицы БД,представление отрисует страницу с ошибкой 404.
from django.views.generic import TemplateView  # позволяет создавать представления на основе класса
from.models import Client, Product, Order


def index(request):
    return render(request, "home2_app/index.html") #  возвращаем шаблон index



def view_for(request):
    my_list = ['apple', 'samsung', 'lada', 'nemiroff', 'zinger']
    my_dict = {
        'продукты': 'животные',
        'для рыбалки': 'для охоты',
        'диваны': 'автомобили',
        'черный рынок': '18+',
        'уцененка': 'телефоны',
        'для дома': 'одежда',
        'для сада': 'тефтельки',
    }
    context = {'my_list': my_list, 'my_dict': my_dict} # ключи должны иметь те имена которые мы используем внутри шаблона, а значения должны совпадать с именами переменных внутри представления в templ_for html так и написано my_list и my_dict
    return render(request, 'home2_app/templ_for.html', context) # принимает запрос пользователя отправляет в шаблон и пробрасывает туда текст


def client_order(request, client_id): # получаем ответ от пользователя и id автора
    client = get_object_or_404(Client, pk=client_id) # извлекаем автора, либо вернет нам автора либо ошибку 404
    order = Order.objects.filter(client=client).order_by('-id')[:5] # если нашли автора, то находим все посты, которые написал автор order_by('-id') отсортирует нам стать по id в обратном порядке [:5] и возьми 5 записей с начала
    return render(request, 'home2_app/order_client.html', {'client': client, 'order': order})


def order_full(request, post_id):
    order = get_object_or_404(Order, pk=post_id)
    return render(request, 'home2_app/order_full.html', {'order': order}) # с помощью функции рендер отрисовываем шаблон post_full передавая туда в качестве контекста этот самый post по ключу пост
