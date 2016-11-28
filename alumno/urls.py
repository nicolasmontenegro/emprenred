from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(r'^$', views.profile, name="ViewMyProfle"),
    url(r'(?P<id>[0-9])/', views.profile, name="ViewProfle"),
]