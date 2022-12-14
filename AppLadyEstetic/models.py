from django.db import models

# Create your models here.

class Inicio(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre+" "+str(self.email)+" "+str(self.telefono)

class Esteticista(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20) 

    def __str__(self):
        return self.nombre+" "+self.apellido
    

class Cosmetologia(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20) 

    def __str__(self):
        return self.nombre+" "+self.apellido
   
class Manicure(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20) 
    
    def __str__(self):
        return self.nombre+" "+self.apellido

class Pacientes(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self): 
        return self.nombre+" "+self.apellido




