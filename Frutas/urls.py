from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('add/', agregar_fruta, name='add_fruit'),
]
