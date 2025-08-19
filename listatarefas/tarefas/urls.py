from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('add/', views.add_tarefas, name='add_tarefas'),
]
