from django.shortcuts import render, redirect
from .models import Academica_curso, Academica_estudiante, Academica_carrera, Academica_matricula
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    cursosListados = Academica_curso.objects.all()
    messages.success(request, '¡Cursos Listados!')
    return render(request, "gestionCursos.html", {"cursos": cursosListados})

def registrarCurso(request):
    if request.method == 'POST':
        codigo=request.POST['txtCodigo']
        nombre=request.POST['txtNombre']
        creditos=request.POST['txtCreditos']
        docente=request.POST['txtDocente']

        curso=Academica_curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos, docente=docente)
        messages.success(request, '¡Curso Registrado!')
        return redirect('/')

def editarCurso(request, codigo):
    curso=Academica_curso.objects.get(codigo=codigo)
    return render(request, "editarCurso.html", {"curso": curso})

def edicionCurso(request):
    if request.method == 'POST':
        codigo=request.POST['txtCodigo']
        nombre=request.POST['txtNombre']
        creditos=request.POST['txtCreditos']
        docente=request.POST['txtDocente']
        
        curso=Academica_curso.objects.get(codigo=codigo)
        curso.nombre=nombre
        curso.creditos=creditos
        curso.docente=docente
        curso.save()
        messages.success(request, '¡Curso Actualizado!')
        return redirect('/')

def eliminarCurso(request, codigo):
    curso=Academica_curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request, '¡Curso Eliminado!')
    return redirect('/')

def carreras(request):
    carrerasListadas = Academica_carrera.objects.all()
    messages.success(request, '¡Carreras Listadas!')
    return render(request, "gestionCarreras.html", {"carreras": carrerasListadas})

def registrarCarrera(request):
    if request.method == 'POST':
        codigo=request.POST['txtCodigo']
        nombre=request.POST['txtNombre']
        duracion=request.POST['txtDuracion']

        carrera=Academica_carrera.objects.create(codigo=codigo, nombre=nombre, duracion=duracion)
        messages.success(request, '¡Carrera Registrada!')
        return redirect('/gestionCarreras/')

def editarCarrera(request, codigo):
    carrera=Academica_carrera.objects.get(codigo=codigo)
    return render(request, "editarCarrera.html", {"carrera": carrera})

def edicionCarrera(request):
    if request.method == 'POST':
        codigo=request.POST['txtCodigo']
        nombre=request.POST['txtNombre']
        duracion=request.POST['txtDuracion']
        
        carrera=Academica_carrera.objects.get(codigo=codigo)
        carrera.nombre=nombre
        carrera.duracion=duracion
        carrera.save()
        messages.success(request, '¡Carrera Actualizado!')
        return redirect('/gestionCarreras/')
    
def eliminarCarrera(request, codigo):
    carrera=Academica_carrera.objects.get(codigo=codigo)
    carrera.delete()
    messages.success(request, '¡Carrera Eliminada!')
    return redirect('/gestionCarreras/')

def estudiante(request):
    estudiantesListados = Academica_estudiante.objects.all()
    estudiante_ejemplo = estudiantesListados.first()  # Obtener un estudiante de ejemplo
    carrerasListadas = Academica_carrera.objects.all()
    messages.success(request, '¡Estudiantes Listados!')
    return render(request, "gestionEstudiantes.html", {"estudiantes": estudiantesListados, "carreras": carrerasListadas, "estudiante_ejemplo": estudiante_ejemplo})

def registrarEstudiante(request):
    if request.method == 'POST':
        dni=request.POST['txtDNI']
        apellidoPaterno=request.POST['txtApellidoPaterno']
        apellidoMaterno=request.POST['txtApellidoMaterno']
        nombres=request.POST['txtNombres']
        fechaNacimiento=request.POST['txtFechaNac']
        sexo=request.POST['txtSexo']
        codigoCarrera=request.POST['txtCarrera']

        # Convertimos el codigoCarrera en un código del objeto Academica_carrera
        carrera_objeto= Academica_carrera.objects.get(codigo=codigoCarrera)

        # Verifica si el checkbox está marcado o no
        if "txtVigente" in request.POST:
            vigencia = True
        else:
        # Si el checkbox no está marcado, establece vigencia en False
            vigencia = False

        estudiante=Academica_estudiante.objects.create(dni=dni, apellidoPaterno=apellidoPaterno,
                                                        apellidoMaterno=apellidoMaterno, 
                                                        nombres=nombres, fechaNacimiento=fechaNacimiento, 
                                                        sexo=sexo, carrera=carrera_objeto, vigencia=vigencia)
        messages.success(request, '¡Estudiante Registrado!')
        return redirect('/gestionEstudiantes/')
    
def editarEstudiante(request, dni):
    estudiante=Academica_estudiante.objects.get(dni=dni)
     # Accede a las opciones de sexo definidas en el modelo
    sexos = estudiante._meta.get_field('sexo').choices
    carrerasListadas = Academica_carrera.objects.all()

    return render(request, "editarEstudiante.html", {"estudiante": estudiante, "sexos": sexos, "carreras": carrerasListadas})

def edicionEstudiante(request):
    if request.method == 'POST':
        dni=request.POST['txtDNI']
        apellidoPaterno=request.POST['txtApellidoPaterno']
        apellidoMaterno=request.POST['txtApellidoMaterno']
        nombres=request.POST['txtNombres']
        fechaNacimiento=request.POST['txtFechaNac']
        sexo=request.POST['txtSexo']
        codigoCarrera=request.POST['txtCarrera']

        # Convertimos el codigoCarrera en un código del objeto Academica_carrera
        carrera_objeto= Academica_carrera.objects.get(codigo=codigoCarrera)

        # Verifica si el checkbox está marcado o no
        if "txtVigente" in request.POST:
            vigencia = True
        else:
        # Si el checkbox no está marcado, establece vigencia en False
            vigencia = False
        
        estudiante=Academica_estudiante.objects.get(dni=dni)
        estudiante.apellidoPaterno=apellidoPaterno
        estudiante.apellidoMaterno=apellidoMaterno
        estudiante.nombres=nombres
        estudiante.fechaNacimiento=fechaNacimiento
        estudiante.sexo=sexo
        estudiante.carrera=carrera_objeto
        estudiante.vigencia=vigencia
        estudiante.save()
        messages.success(request, '¡Estudiante Actualizado!')
        return redirect('/gestionEstudiantes/')
    
def eliminarEstudiante(request, dni):
    estudiante=Academica_estudiante.objects.get(dni=dni)
    estudiante.delete()
    messages.success(request, '¡Estudiante Eliminado!')
    return redirect('/gestionEstudiantes/')

def matriculas(request):
    matriculasListadas = Academica_matricula.objects.all()
    estudiantesListados = Academica_estudiante.objects.all()
    cursosListados = Academica_curso.objects.all()

    messages.success(request, '¡Matriculas Listadas!')
    return render(request, "gestionMatriculas.html", {"matriculas": matriculasListadas, "estudiantesListados": estudiantesListados, "cursosListados": cursosListados})

def registrarMatricula(request):
    if request.method == 'POST':
        codigoEstudiante=request.POST['txtEstudiante']
        codigoCurso=request.POST['txtCurso']

        # Convertimos codigoEstudiante en un código del objeto Academica_estudiante
        estudiante_objeto= Academica_estudiante.objects.get(dni=codigoEstudiante)

        # Convertimos codigoCurso en un código del objeto Academica_curso
        curso_objeto= Academica_curso.objects.get(codigo=codigoCurso)

        matricula=Academica_matricula.objects.create(estudiante=estudiante_objeto,
                                                        curso=curso_objeto)
        messages.success(request, '¡Matricula Registrada!')
        return redirect('/gestionMatriculas/')
    
def eliminarMatricula(request, id):
    matricula=Academica_matricula.objects.get(id=id)
    matricula.delete()
    messages.success(request, '¡Matrícula Eliminada!')
    return redirect('/gestionMatriculas/')
    
def formularioContacto(request):
    return render(request, "formularioContacto.html")

def contactar(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " / Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["contacto@joseluweb.com.ar"]

        # Verifica si el checkbox está marcado
        if "gridCheck" in request.POST:
            # Si está marcado, añade la dirección de email del remitente para enviar una copia
            email_para.append(request.POST["txtEmail"])

        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "contactoExitoso.html")
    return render(request, "formularioContacto.html")