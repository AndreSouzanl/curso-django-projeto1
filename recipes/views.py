from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(resquest):
    return HttpResponse("HOME 1")

def contato(resquest):
    return HttpResponse("CONTATO")

def sobre(resquest):
    return HttpResponse("SOBRE")


