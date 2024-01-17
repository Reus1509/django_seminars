#from django.shortcuts import render
from django.http import HttpResponse
from random import choice
from .models import Coin, Author, Post


def orel_and_reshka(request):
    my_list = ['Орел', 'Решка']
    result = choice(my_list)
    if result == 'Орел':
        res = 1
    else:
        res = 0
    coin = Coin(side=res)
    coin.save()

    return HttpResponse(f'Выпало: {result}, Статистика: {Coin.get_data(5)}')


def authors_view(request):
    authors = Author.objects.all()
    res_str = '<br>'.join([str(author) for author in authors])
    return HttpResponse(res_str)


def post_view(request):
    posts = Post.objects.all()
    res_str = '<br>'.join([str(post) for post in posts])
    return HttpResponse(res_str)
