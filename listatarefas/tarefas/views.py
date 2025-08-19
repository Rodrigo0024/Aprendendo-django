from django.shortcuts import render, redirect, get_object_or_404
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


def remover_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefas, id=tarefa_id)
    tarefa.delete()
    return redirect('lista_tarefas')

def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefas, id=tarefa_id)

    if request.method == "POST":
        titulo = request.POST.get("title")
        concluida = request.POST.get("completed") == "on"
        tarefa.title = titulo
        tarefa.completed = concluida
        tarefa.save()
        return redirect("lista_tarefas")

    return render(request, "tarefas/editar_tarefa.html", {"tarefa": tarefa})
