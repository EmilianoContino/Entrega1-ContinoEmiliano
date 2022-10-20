from importlib.resources import path
from django.urls import path, include
from accounts import views



urlpatterns = [
    
    path('login/', login, name='login'),
    path()
    
]