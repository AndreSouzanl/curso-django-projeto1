from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe

# Create your views here.

def home(resquest):
    recipes = Recipe.objects.filter(
         is_published = True
    ).order_by('-id')
    context={
        'recipes': recipes,
    }
    return render(resquest, 'recipes/pages/home.html',context) 

def category(resquest, category_id):
    recipes = Recipe.objects.filter(
        category_id=category_id,
        is_published = True
    ).order_by('-id')
    context={
        'recipes': recipes,
    }
    return render(resquest, 'recipes/pages/category.html',context) 

def recipe(resquest, id):
    context={
        'recipe': make_recipe(),
        'is_detail_page': True
    }
    return render(resquest, 'recipes/pages/recipe-view.html',context) 





