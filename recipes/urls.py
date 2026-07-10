from django.urls import path
from recipes.views import home, contato, sobre

# return HttpResponse
# http request -> urls.py -> view -> template -> response

urlpatterns = [
    path('', home),         # /HOME/
    path('sobre/', sobre),   # /SOBRE/
    path('contato/', contato), # /CONTATO/
    
]
