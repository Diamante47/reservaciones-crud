# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nuevoCampista/', views.nuevoCampista, name='nuevo_Campista'),
    path('listadoCampistas/', views.listadoCampistas, name='listado_Campistas'),
    path('guardarCampista/', views.guardarCampista, name='guardar_usuario'),
    path('eliminarCampista/<int:id>/', views.eliminarCampista, name='eliminar_Campista'),
    path('editarCampista/<int:id>/', views.editarCampista, name='editar_campista'),
    path('procesarEdicionCampista/', views.procesarEdicionCampista, name='procesarEdicionCampista'),

    path('listadoReservaciones/', views.listadoReservaciones, name="listadoReservaciones"),
    path('nuevaReservacion/', views.nuevaReservacion, name="nuevaReservacion"),
    path('guardarReservacion/', views.guardarReservacion, name='guardarReservacion'),
    path('eliminarReservacion/<id>', views.eliminarReservacion, name='eliminarReservacion'),
    path('editarReservacion/<int:id>/', views.editarReservacion, name='editarReservacion'),
    path('procesarEdicionReservacion/', views.procesarEdicionReservacion, name='procesarEdicionReservacion'),
]
