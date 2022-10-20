
from curses.ascii import HT
from django.contrib import admin
from django.urls import path

from django.http import HttpResponse


def home(r):
    return HttpResponse('<h1>done</h1>')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home)
]
