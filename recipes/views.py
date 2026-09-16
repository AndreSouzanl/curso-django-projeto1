from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recipe

# Create your views here.

def home(resquest):
    recipes =Recipe.objects.filter(
        is_published = True
        ).order_by('-id')
    
    context={
        'recipes': recipes,
    }
    return render(resquest, 'recipes/pages/home.html',context) 

def category(resquest, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
        category_id=category_id,
        is_published = True
        ).order_by('-id'))
    context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category |'
    }
    return render(resquest, 'recipes/pages/category.html',context) 

def recipe(resquest, id):
    recipe = get_object_or_404( Recipe, pk=id, is_published = True)
    
    context={
        'recipe': recipe,
        'is_detail_page': True
    }
    return render(resquest, 'recipes/pages/recipe-view.html',context) 





