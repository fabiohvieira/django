from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('<h1>Lista Clientes</h1>')

def show(request):
    return HttpResponse('<h1>Detalhes do Cliente</h1>')

