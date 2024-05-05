from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('editarCurso/<codigo>', views.editarCurso),
    path('edicionCurso/', views.edicionCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
    path('gestionCarreras/', views.carreras),
    path('registrarCarrera/', views.registrarCarrera),
    path('editarCarrera/<codigo>', views.editarCarrera),
    path('edicionCarrera/', views.edicionCarrera),
    path('eliminarCarrera/<codigo>', views.eliminarCarrera),
    path('gestionEstudiantes/', views.estudiante),
    path('editarEstudiante/<dni>', views.editarEstudiante),
    path('edicionEstudiante/', views.edicionEstudiante),
    path('eliminarEstudiante/<dni>', views.eliminarEstudiante),
    path('registrarEstudiante/', views.registrarEstudiante),
    path('gestionMatriculas/', views.matriculas),
    path('registrarMatricula/', views.registrarMatricula),
    path('eliminarMatricula/<id>', views.eliminarMatricula),
    path('formularioContacto/', views.formularioContacto),
    path('contactar/', views.contactar),
]