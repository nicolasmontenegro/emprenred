from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, permission_required
import django

from . import models as modelEtiqueta

@login_required
def pagesAll(request, inputEtiqueta):
    #Get anuncios
    etiquetaObject = modelEtiqueta.Etiqueta.objects.get(nombre__exact=inputEtiqueta)
    etiquetaAnunciosList = etiquetaObject.anuncio_set.all()

    paginatorAnuncios = Paginator(etiquetaAnunciosList, 5)
    page = request.GET.get('page')
    try:
        etiquetaAnunciosList = paginatorAnuncios.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        etiquetaAnunciosList = paginatorAnuncios.page(paginatorAnuncios.num_pages)

    #Get usuarios

    etiquetaAlumnoList = etiquetaObject.alumno_set.all()
    paginatorAlumnos = Paginator(etiquetaAlumnoList, 5)
    page = request.GET.get('page')
    try:
        etiquetaAlumnoList = paginatorAlumnos.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        etiquetaAlumnoList = paginatorAlumnos.page(paginatorAlumnos.num_pages)


    return render(request, 'site/tagList.html', {'anuncios': etiquetaAnunciosList, 'alumnos': etiquetaAlumnoList,'etiqueta': etiquetaObject})

@login_required
def pagesAnuncios(request, inputEtiqueta):
    etiquetaObject = modelEtiqueta.Etiqueta.objects.get(nombre__exact=inputEtiqueta)
    etiquetaList = etiquetaObject.anuncio_set.all()

    paginator = Paginator(etiquetaList, 25)
    page = request.GET.get('page')
    try:
        etiquetaList = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        etiquetaList = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        etiquetaList = paginator.page(paginator.num_pages)

    return render(request, 'site/tagAnunciosList.html', {'anuncios': etiquetaList, 'etiqueta': etiquetaObject})

@login_required
def pagesAlumnos():
    pass