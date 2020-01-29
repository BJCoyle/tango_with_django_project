#Barry Coyle
#29/01/2020
#Rango URL mappings

from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name = 'index'),
]
