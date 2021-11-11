from django.db import models

# Create your models here.
class Conductor(models.Model):
    nombres=models.CharField(max_length=50)
    apellidopaterno=models.CharField(max_length=50)
    apellidoMaterno=models.CharField(max_length=50)
    estadoCivil=models.CharField(max_length=8)
    sexo=models.CharField(max_length=10)
    direccion=models.CharField(max_length=50)
    celular=models.CharField(max_length=15)
    correo=models.CharField(max_length=25)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = ("Conductor")
        verbose_name_plural = ("Conductors")

    def __str__(self):
        return self.nombres



class Maquinaria(models.Model):
    placa=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    caballosFuerza=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    motor=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)
    conductor=models.ForeignKey("Conductor", on_delete=models.CASCADE)


    class Meta:
        verbose_name = ("Maquinaria")
        verbose_name_plural = ("Maquinarias")

    def __str__(self):
        return self.placa