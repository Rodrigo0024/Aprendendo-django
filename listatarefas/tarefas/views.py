from django.shortcuts import render, redirect
from .models import Tarefas

def lista_tarefas(request):
    tarefas = Tarefas.objects.all()
    return render(request, 'tarefas/lista_tarefas.html', {'tarefas': tarefas})

def add_tarefas(request):
    if request.method == 'POST':
        title = request.POST['title']
        Tarefas.objects.create(title=title)
        return redirect('lista_tarefas')
    return render(request, 'tarefas/add_tarefas.html')
