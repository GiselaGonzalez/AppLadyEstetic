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

def Esteticista(request):
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

    return render(request,"AppLadyEstetic/Esteticista.html", {"form":formulario})

def Cosmetologia(request):

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

    return render(request,"AppLadyEstetic/Cosmetologia.html", {"form":formulario})
            

def Manicure(request):

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

    return render(request,"AppLadyEstetic/Manicure.html", {"form":formulario})
            


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
        apellido=request.GET["apellido"]

        pacientes=Pacientes.objects.filter(apellido=apellido)
        return render (request,"AppLadyEstetic/resultadosBusqueda.html",{"Pacientes":Pacientes})

    else:
        return render(request, "AppLadyEstetic/BuscarPaciente.html", {"mensaje":"Ingrese un apellido"})

    return render



