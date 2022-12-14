from django.urls import path
from AppLadyEstetic.views import *
    
urlpatterns= [  
    path("",Inicio,name="Inicio"),
    path("Contacto/",Contacto,name="Contacto"),
    path("Esteticista/",Esteticista,name="Esteticista"),
    path("Cosmetologia/",Cosmetologia,name="Cosmetologia"),
    path("Manicure/",Manicure,name="Manicure"),
    path("Pacientes/",Pacientes,name="Pacientes"),
    path("Reservar_Turno/",Reservar_Turno,name="Reservar_Turnos"),
    path("PacientesFormulario/",PacientesFormulario,name="PacientesFormulario"),
     path("BuscarPaciente/",BuscarPaciente,name="BuscarPaciente"),
    path("Buscar/",Buscar,name="Buscar"),
    
   


 ]

