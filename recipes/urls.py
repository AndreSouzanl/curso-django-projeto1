from django.urls import path
from recipes.views import home

# return HttpResponse
# http request -> urls.py -> view -> template -> response

urlpatterns = [
    path('', home),         # /HOME/
]
