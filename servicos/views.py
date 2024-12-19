from django.shortcuts import render
from .forms import FormServico
from django.http import HttpResponse
from .models import Servico

# Create your views here.


def novo_servico(request):
  if request.method == "GET":
    form = FormServico()
    return render(request, 'novo_servico.html', {'form': form})
  elif request.method == "POST":
    form = FormServico(request.POST)

    if form.is_valid():
      form.save()
      return HttpResponse('Salvo com sucesso')
    else:
      return render(request, 'novo_servico.html', {'form': form})
    
def listar_servico(request):
  if request.method == "GET":
    servicos = Servico.objects.all()
    return render(request, 'listar_servico.html', {'servicos': servicos})