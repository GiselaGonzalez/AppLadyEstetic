from django.shortcuts import render
from .models import*
from django.http import HttpResponse
from django.shortcuts import render
from AppLadyEstetic.forms import PacientesForm
from AppLadyEstetic.forms import CosmetologiaForm
from AppLadyEstetic.forms import EsteticistaForm
from AppLadyEstetic.forms import ManicureForm


# Create your views here.

def Inicio(request):
    return render (request, "AppLadyEstetic/Inicio.html")

def Contacto(request):
    return render (request, "AppLadyEstetic/Contacto.html")

def CrearEsteticista(request):
    if request.method=="POST":
        form=EsteticistaForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
        
            Nombre=informacion["nombre"]
            Apellido=informacion["apellido"]
            cosmetologia=Esteticista(nombre=Nombre, apellido=Apellido)
            cosmetologia.save()
            return render (request, "AppLadyEstetic/Inicio.html")
    else:
        formulario=EsteticistaForm()

    return render(request,"AppLadyEstetic/CrearEsteticista.html", {"form":formulario})

def CrearCosmetologia(request):

    if request.method=="POST":
        form=CosmetologiaForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
        
            Nombre=informacion["nombre"]
            Apellido=informacion["apellido"]
            cosmetologia=Cosmetologia(nombre=Nombre, apellido=Apellido)
            cosmetologia.save()
            return render (request, "AppLadyEstetic/Inicio.html")
    else:
        formulario=CosmetologiaForm()

    return render(request,"AppLadyEstetic/CrearCosmetologia.html", {"form":formulario})
            

def CrearManicure(request):

    if request.method=="POST":
        form=ManicureForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
        
            Nombre=informacion["nombre"]
            Apellido=informacion["apellido"]
            cosmetologia=Manicure(nombre=Nombre, apellido=Apellido)
            cosmetologia.save()
            return render (request, "AppLadyEstetic/Inicio.html")
    else:
        formulario=ManicureForm()

    return render(request,"AppLadyEstetic/CrearManicure.html", {"form":formulario})
            


def Reservar_Turno(request):
    return render(request,"AppLadyEstetic/Reservar_Turno.html")

def PacientesFormulario(request):

    if request.method=="POST":
        form=PacientesForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
 
            Nombrecito=informacion["nombre"]
            Apellido=informacion["apellido"]
            Email=informacion["email"]
            Telefono=informacion["telefono"]

            paciente = Pacientes (nombre=Nombrecito,apellido=Apellido,email=Email,telefono=Telefono)
            paciente.save()
            return render (request, "AppLadyEstetic/Inicio.html",{"mensaje":"Los datos del paciente se guardaron correctamente"})
    
    else:
        formulario=PacientesForm()

    return render(request, "AppLadyEstetic/PacientesFormulario.html", {"form":formulario})


def BuscarPaciente(request):
    return render(request, "AppLadyEstetic/BuscarPaciente.html")


def Buscar(request):

    if request.GET["apellido"]:
       apellido= request.GET['apellido']
       paciente = Pacientes.objects.filter(apellido__icontains=apellido)

       return render(request, "AppLadyEstetic/resultadosBusqueda.html",{"pacientes":paciente, "apellido":apellido})
    else:

      respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

    #respuesta= f" Estoy buscando el Paciente: {request.GET ['apellido'] }"
    

    

  




