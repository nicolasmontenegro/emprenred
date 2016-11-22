from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^crear', views.create, name='CrearAnuncio'),	
	url(r'(?P<id>[0-9])/', views.detail, name='DetalleAnuncio'),	
	url(r'^$', views.pages, name='Anuncios'),

]