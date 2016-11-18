from django.db import models

from etiqueta import models as modelEtiqueta
from alumno import models as modelAlumno

class Anuncio(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(blank=False, max_length=50)
    fechaCreacion = models.DateField()
    tiempoVencimiento = models.DurationField()
    etiqueta = models.ManyToManyField(modelEtiqueta.Etiqueta, blank=True)
    alumno = models.ForeignKey(modelAlumno.Alumno, blank=False)

    class Meta:
        verbose_name = "Anuncio"
        verbose_name_plural = "Anuncios"

    def __str__(self):
        return self.id