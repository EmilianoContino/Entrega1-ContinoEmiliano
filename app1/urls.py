from importlib.resources import path
from django.urls import path
from app1 import views


urlpatterns = [
    path('', views.index, name='inicio'),
    # path("hola/", views.hola, name='hola'),
    # path("mi-template/", views.mi_template),
    # path('crear-familiar/<str:nombre>/<str:apellido>/<str:edad>/', views.crear_familiar),
    # path('ver-familiares/', views.ver_familiares, name='ver_familiares'),
]
