"""
URL configuration for Mascotas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Bd_mascotas import views as bd_views

from Bd_mascotas.views import BlogListView, BlogCreate, ContactoCreate

urlpatterns = [
    #LOGICA DE NEGOCIO
    path('admin/', admin.site.urls),
    path('',bd_views.main , name="index" ),
    
    #path("blog/", bd_views.blog, name="blog"),
    path("portafolio/", bd_views.portafolio, name="portafolio"),
    path("services/", bd_views.services, name="services"),
    path("ingresar/", bd_views.login, name="login"),
    path("registrou/",bd_views.registrou, name="registrou"),


    #CRUD PARA LA TABLA POST
    path('blog/', BlogListView.as_view(), name='blog'),
    path('crear/',BlogCreate.as_view(), name="crearposter"),
    path("contacto/", ContactoCreate.as_view(), name="contacto"),


         
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

