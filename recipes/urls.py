from django.urls import path
from . import views

# return HttpResponse
# http request -> urls.py -> view -> template -> response

# recipes:recipe
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),         # /HOME/
    path('recipes/<int:id>/', views.recipe, name='recipe'),  # /recipes/1/      
]
