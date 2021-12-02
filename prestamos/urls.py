from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('',views.ListarPrestamos, name='ListarPrestamos'),
   path('filtrar', views.FiltroPorID, name="FiltroPorID"),
   path('Prestamo/new', views.NuevoPrestamo, name="NuevoPrestamo"),
   path('EliminarPrestamo/<id>',views.EliminarPrestamo,name="EliminarPrestamo"),
   path('ModificarPrestamo/<id>',views.ModificarPrestamo,name="ModificarPrestamo"), 
]