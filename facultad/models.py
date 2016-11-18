from django.db import models

class Facultad(models.Model):

    id = models.AutoField(primary_key=True)
    cod = models.CharField(blank=False, max_length=5)
    nombre = models.CharField(blank=False, max_length=50)
    descripcion = models.TextField(blank=True)
    logo = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = "Facultad"
        verbose_name_plural = "Facultades"

    def __str__(self):
        return self.nombre

class Carrera(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(blank=False, max_length=50)
    facultad = models.ForeignKey("Facultad", blank=False)

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"

    def __str__(self):
        return self.nombre
    