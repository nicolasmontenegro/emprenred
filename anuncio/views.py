from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import DateTimeField, ExpressionWrapper, F
from django.http import Http404
import django

from . import models as modelAnuncio
from . import forms as formAnuncio

templateObject = {
    "HeadTitle":{
        "title": "Timp Transportes",
        "section": "",
    },  
    "isHome": True,
}

@login_required
def pages(request):
    anunciosList = modelAnuncio.Anuncio.objects.all()
    try:   
        expression = F('fechaCreacion') + F('tiempoVencimiento')
        anunciosList = anunciosList.annotate(delta=ExpressionWrapper(expression, DateTimeField()))
        anunciosList = anunciosList.filter(delta__gt=django.utils.timezone.now()) 
    except:
        raise Http404("No hay anuncios que mostrar.")

    paginator = Paginator(anunciosList, 25)
    page = request.GET.get('page')
    try:
        anunciosList = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        anunciosList = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        anunciosList = paginator.page(paginator.num_pages)

    return render(request, 'site/announcementList.html', {'anuncios': anunciosList})

@login_required
def create(request):
    if request.method == "POST":
        form = formAnuncio.AnuncioForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            post.save()
            return redirect("DetalleAnuncio", id=post.id)
        else:
            print (form.errors)
    else:
        form = formAnuncio.AnuncioForm()
    return render(request, 'site/announcementCreate.html', {'form': form})


@login_required
def detail(request, id):
    anuncio = get_object_or_404(modelAnuncio.Anuncio, id=id)
    return render(request, 'site/announcement.html', {"anuncio": anuncio})