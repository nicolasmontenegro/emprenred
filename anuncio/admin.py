from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.db.models import DateTimeField, ExpressionWrapper, F
import django
import datetime as datetime #bad joke

from . import models

class VencimientoFilter(admin.SimpleListFilter):
    title = _('vencido')
    parameter_name = 'vencido'
    def lookups(self, request, model_admin):        
        return (
            ('vencidoTrue', _('Vencidos')),
            ('vencidoFalse', _('Vigente')),
        )

    def queryset(self, request, queryset):
        expression = F('fechaCreacion') + F('tiempoVencimiento')
        queryset = queryset.annotate(delta=ExpressionWrapper(expression, DateTimeField()))
        if self.value() == 'vencidoTrue':
            return queryset.filter(delta__lte=django.utils.timezone.now()) 
        if self.value() == 'vencidoFalse':
            return queryset.filter(delta__gt=django.utils.timezone.now()) 

class AnuncioAdmin(admin.ModelAdmin):
    #fields = ('titulo,' 'fechaCreacion', 'tiempoVencimiento',) 
    list_display = ('id', 'fechaCreacion', 'tiempoVencimiento', 'alumno',) 
    list_filter = (VencimientoFilter, "alumno",)
    ordering = ('-id',)

admin.site.register(models.Anuncio, AnuncioAdmin)

# Register your models here.


