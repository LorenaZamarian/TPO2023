from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('hola_tienda', views.hola_tienda, name='hola'),
    path('productos', views.productos, name='productos'),
    path('api_productos/',views.api_productos,name="api_productos"),
]
