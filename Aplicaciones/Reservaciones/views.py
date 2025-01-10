from django.shortcuts import get_object_or_404, redirect, render
from.models import Campista, Reservacion
from django.contrib import messages
# Create your views here.
def inicio (request): #funcion para presentar en pantalla el codigo html del template inicio.html
    return render(request,'inicio.html')

                        #Usuarios
def nuevoCampista (request):
    return render(request,'nuevoCampista.html')

def listadoCampistas(request):
    campistasBdd=Campista.objects.all()
    return render(request,'listadoCampistas.html',{'campistas':campistasBdd})

def guardarCampista(request):
    nombre=request.POST['txt_nombre']
    correo=request.POST['txt_correo']
    telefono=request.POST['txt_telefono']
    direccion=request.POST['txt_direccion']
    nuevoCampista=Campista.objects.create(nombre=nombre, correo=correo, telefono=telefono, direccion=direccion)
    messages.success(request,"Campista Guardado Exitosamente")
    return redirect('/listadoCampistas')

def eliminarCampista(request,id):
    campistaEliminar=Campista.objects.get(id=id)
    campistaEliminar.delete()
    messages.success(request,"Campista eliminado Exitosamente")
    return redirect('/listadoCampistas')

def editarCampista(request, id):
    campistaEditar = get_object_or_404(Campista, id=id)
    return render(request, "editarCampista.html", {'campista': campistaEditar})

def editarCampista(request,id):
    campistaEditar=Campista.objects.get(id=id)
    return render(request,"editarCampista.html",{'campista':campistaEditar})


def procesarEdicionCampista(request):
    campista=Campista.objects.get(id=request.POST['id'])
    nombre=request.POST['txt_nombre']
    correo=request.POST['txt_correo']
    telefono=request.POST['txt_telefono']
    direccion=request.POST['txt_direccion']
    campista.nombre=nombre
    campista.correo=correo
    campista.telefono=telefono
    campista.direccion=direccion
    campista.save()
    messages.success(request,"Datos Actulizados")
    return redirect('/listadoCampistas')

                        #Reservaciones

def listadoReservaciones(request):
    reservacionesBdd=Reservacion.objects.all()
    return render(request,'listadoReservaciones.html',{'reservacionesBdd':reservacionesBdd})

def nuevaReservacion(request):
   campistareservacion = Campista.objects.all()
   return render(request,'nuevaReservacion.html',{'campistareservacion': campistareservacion})

def guardarReservacion(request):
    if request.method == 'POST':
        campista_id = request.POST['campista']
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_fin']
        tipo_de_alojamiento = request.POST.getlist('tipo_de_alojamiento')  # Obtener la lista de valores
        numero_de_personas = request.POST['numero_de_personas']
        estado_de_la_reserva = request.POST.getlist('estado_de_la_reserva')  # Obtener la lista de valores
        observacion = request.POST['observacion']

        campista = Campista.objects.get(id=campista_id)

        nuevaReservacion = Reservacion.objects.create(
            campista=campista,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            tipo_de_alojamiento=','.join(tipo_de_alojamiento),  # Unir la lista en una cadena
            numero_de_personas=numero_de_personas,
            estado_de_la_reserva=','.join(estado_de_la_reserva),  # Unir la lista en una cadena
            observacion=observacion
        )

        messages.success(request, "Se guardó correctamente.")
        return redirect('listadoReservaciones')

def eliminarReservacion(request,id):
    reservacionEliminar=Reservacion.objects.get(id=id)
    reservacionEliminar.delete()
    messages.success(request,"Se ha eliminado correctamente.")
    return redirect('listadoReservaciones')

def editarReservacion(request, id):
    reservacion = get_object_or_404(Reservacion, id=id)
    campistas = Campista.objects.all()  # Obtener todos los campistas para el select
    context = {'reservacion': reservacion, 'campistas': campistas}
    return render(request, "editarReservacion.html", context)

def procesarEdicionReservacion(request):
    if request.method == 'POST':
        reservacion_id = request.POST['id']
        reservacion = get_object_or_404(Reservacion, id=reservacion_id)

        # Obtener los datos del formulario
        campista_id = request.POST['campista']
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_fin']
        tipo_de_alojamiento = request.POST['tipo_de_alojamiento']
        numero_de_personas = request.POST['numero_de_personas']
        estado_de_la_reserva = request.POST['estado_de_la_reserva']
        observacion = request.POST['observacion']

        # Obtener el objeto Campista
        campista = get_object_or_404(Campista, id=campista_id)

        # Actualizar los datos de la reservacion
        reservacion.campista = campista
        reservacion.fecha_inicio = fecha_inicio
        reservacion.fecha_fin = fecha_fin
        reservacion.tipo_de_alojamiento = tipo_de_alojamiento
        reservacion.numero_de_personas = numero_de_personas
        reservacion.estado_de_la_reserva = estado_de_la_reserva
        reservacion.observacion = observacion

        reservacion.save()
        messages.success(request, "Reservación actualizada correctamente")
        return redirect('listadoReservaciones')  # Reemplaza con el nombre de tu vista de listado
    else:
        return redirect('listadoReservaciones')
