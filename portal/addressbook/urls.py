from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [ 
    path('addressbook/new', views.index, name='index'),
    path('addressbook/2', views.show, name="show"),
]