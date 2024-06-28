from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from .models import Post, Categoria, Contacto, Servicio, Producto
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from  .forms import BlogForms, ContactoForms


def main(request):
    template=loader.get_template("Bd_mascotas/index.html")
    return HttpResponse(template.render())

"""def blog(request):
    post = Post.objects.all()
   
    return render (request, "Bd_mascotas/blog.html",{"post":post})"""

def portafolio (request):
    producto = Producto.objects.all()
    return render (request, "Bd_mascotas/portfolio.html",{"productos":producto})

def services (request):
    servicio= Servicio.objects.all()
    return render (request, "Bd_mascotas/services.html",{"servicios":servicio})

def login (request):
    return render (request,"Bd_mascotas/ingresar.html")

def registrou(request):
    return render(request,"Bd_mascotas/registro.html")

#CBV EN LA CRUD: LISTVIEW - POST Y CATEGORIA DEL TEMPLATE BLOG

class BlogListView(ListView):
    model: Post 
    paginate_by = 1

    def get_queryset(self):
        return Post.objects.all()
    
    #envia informacion adicional la cual sirve para poder paginar
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

#CBV EN LA CRUD: CREATEVIEW - POST Y CATEGORIA DEL TEMPLATE BLOG
class BlogCreate(CreateView):
    model= Post #tabla
    form_class=BlogForms
    template_name='Bd_mascotas\CreateBlog.html'
    success_url= reverse_lazy('blog')

class ContactoCreate(CreateView):
    model= Contacto
    form_class = ContactoForms
    template_name ='Bd_mascotas\contact.html'
    success_url= reverse_lazy('contacto')