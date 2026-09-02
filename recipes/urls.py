from django.urls import path
from . import views

# return HttpResponse
# http request -> urls.py -> view -> template -> response

urlpatterns = [
    path('', views.home),         # /HOME/
    path('recipes/<int:id>/', views.recipe),         
]
