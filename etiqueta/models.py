from django.db import models

class Categoria(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(blank=False, max_length=50)
    descrpcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre
    
class Etiqueta(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(blank=False, max_length=50)
    categoria = models.ForeignKey(Categoria, blank=True)

    class Meta:
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiquetas"

    def __str__(self):
        return self.nombre

# Create your models here.
