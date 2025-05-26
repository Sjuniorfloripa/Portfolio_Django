from django.shortcuts import render
from portfolio.dados import habilidades, projetos


def home(request):
    return render(request, 'home.html', {'habilidades': habilidades})

def lista_projetos(request):
    return render(request, 'projetos.html', {'projetos': projetos})

def detalhes_projeto(request, id):
    projeto = projetos.get(id)
    return render(request, 'detalhes_projeto.html', {'projeto': projeto})