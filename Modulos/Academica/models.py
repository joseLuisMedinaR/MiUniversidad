from django.db import models

# Create your models here.
class Academica_carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    duracion = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt = "{0} (Duración: {1} años(s))"
        return txt.format(self.nombre, self.duracion)

class Academica_estudiante(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellidoPaterno = models.CharField(max_length=35, null=False)
    apellidoMaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35, null=False)
    fechaNacimiento = models.DateField()
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('NB', 'No Binario')
    ]
    sexo = models.CharField(max_length=2, choices=sexos, default='NB')
    carrera = models.ForeignKey(Academica_carrera, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    def nombreCompleto(self):
        txt = "{0} {1}, {2} "
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)
    
    def __str__(self):
        txt = "{0} / Carrera: {1} / {2}"
        if self.vigencia:
            estadoEstudiante = "VIGENTE"
        else:
            estadoEstudiante = "DE BAJA"

        return txt.format(self.nombreCompleto(), self.carrera, estadoEstudiante)
    
class Academica_curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100, null=False)

    def __str__(self):
        txt = "{0} ({1}) / Docente: {2}"
        return txt.format(self.nombre, self.codigo, self.docente)

class Academica_matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Academica_estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Academica_curso, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt = "{0} matriculad{1} en el curso {2} / Fecha: {3}"
        if self.estudiante.sexo == "F":
            letraSexo = "a"
        elif self.estudiante.sexo == "M":
            letraSexo = "o"
        else:
            letraSexo = "e"

        fecMat = self.fechaMatricula.strftime("%A %d/%m/%Y %H:%M:%S")
        return txt.format(self.estudiante.nombreCompleto(), letraSexo, self.curso, fecMat)