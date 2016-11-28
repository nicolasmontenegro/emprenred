from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^(?P<inputEtiqueta>[\w\-]+)/$', views.pagesAll, name="DetalleEtiqueta"),
	url(r'^(?P<inputEtiqueta>[\w\-]+)/anuncios$', views.pagesAnuncios, name="EtiquetaAnuncios"),
	url(r'^(?P<inputEtiqueta>[\w\-]+)/alumnos$', views.pagesAlumnos, name="EtiquetaAlumnos"),
]