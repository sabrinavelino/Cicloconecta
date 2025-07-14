
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('gabinete/', views.gabinete, name='gabinete'),
    path('hd/', views.hd, name='hd'),
    path('memoria/', views.memoria, name='memoria'),
    path('meus-anuncios/', views.meus_anuncios, name='meus_anuncios'),
    path('perifericos/', views.perifericos, name='perifericos'),
    path('novo_anuncios/', views.novo_anuncios, name='novo_anuncios'),
    path('usuarios/', include('usuarios.urls')),  
]
