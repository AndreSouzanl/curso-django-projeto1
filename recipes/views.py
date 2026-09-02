from django.shortcuts import render

# Create your views here.

def home(resquest):
    context={
        'name': 'Andre Luiz de Souza',
    }
    return render(resquest, 'recipes/pages/home.html',context) 

def recipe(resquest, id):
    context={
        'name': 'Andre Luiz de Souza',
    }
    return render(resquest, 'recipes/pages/recipe-view.html',context) 





