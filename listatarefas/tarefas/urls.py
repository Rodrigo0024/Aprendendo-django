from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('add/', views.add_tarefas, name='add_tarefas'),
    path('remover/<int:tarefa_id>/', views.remover_tarefa, name='remover_tarefa'),
]
