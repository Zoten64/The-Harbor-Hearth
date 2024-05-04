from django.shortcuts import render
from django.views import generic
from menu.models import Menu

# Create your views here.

class Index(generic.ListView):
    queryset = Menu
    template_name = 'home/index.html'
