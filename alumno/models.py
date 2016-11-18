from django.db import models
from django.contrib.auth.models import User

from facultad import models as modelFalcultad
from etiqueta import models as modelEtiqueta

class Alumno(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    annoIngreso = models.PositiveSmallIntegerField(blank=False)
    telefono = models.PositiveSmallIntegerField(blank=False)
    carrera = models.ForeignKey(modelFalcultad.Carrera, blank=False)
    etiquetas = models.ManyToManyField(modelEtiqueta.Etiqueta, blank=True)#, limit_choices_to = {"etiqueta__id":10} )
    verificador = models.CharField(blank=True, max_length=1)



    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __str__(self):
        nombreCompleto = self.user.first_name + " " + self.user.last_name
        return nombreCompleto