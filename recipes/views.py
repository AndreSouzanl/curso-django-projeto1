from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(resquest):
    context={
        'name': 'Andre Luiz de Souza',
    }
    return render(resquest, 'recipes/home.html',context) 

def contato(resquest):
    return HttpResponse("CONTATO")

def sobre(resquest):
    return HttpResponse("SOBRE")


