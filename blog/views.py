from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {'title': 'Главная страница'}
    return render(request, template_name='blog/index.html', context=context)

def about(request):
    # context = {'title': 'Главная страница'}
    # return render(request, template_name='blog/about.html', context=context)
    return HttpResponse('<h2>О сайте</h2>')