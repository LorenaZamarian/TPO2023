from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_administracion, name='inicio'),
    path('administracion/signin/', views.signin, name='ingresar'),
    path('administracion/signup/', views.signup, name='registrarse'),
    path('administracion/signout/', views.signout, name='logout'),
]
