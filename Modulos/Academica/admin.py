from django.contrib import admin
from Modulos.Academica.models import *

# Register your models here.
admin.site.register(Academica_carrera)
admin.site.register(Academica_estudiante)
admin.site.register(Academica_curso)
admin.site.register(Academica_matricula)