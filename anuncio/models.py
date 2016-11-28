from django.db import models
import django

from etiqueta import models as modelEtiqueta

from django.contrib.auth.models import User

class Anuncio(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(blank=False, max_length=50)
    descripcion = models.TextField(blank=True, max_length=2000)
    fechaCreacion = models.DateTimeField(default=django.utils.timezone.now)
    tiempoVencimiento = models.DurationField(default="15 00:00:00")
    etiqueta = models.ManyToManyField(modelEtiqueta.Etiqueta, blank=True)
    usuario = models.ForeignKey(User, null=True)

    class Meta:
        verbose_name = "Anuncio"
        verbose_name_plural = "Anuncios"

    def __str__(self):
        return "Anuncio " + str(self.id) 