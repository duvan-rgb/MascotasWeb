from django.contrib import admin
from .models import Usuario,Mascota,MascotaServicio,Servicio,ProductoUsuario,Producto,Categoria,Post,Contacto

class MascotaAdmin(admin.ModelAdmin):
    list_display = ("id_mascota","tipo","raza","nom_mas","fecha_naci","foto","id_usuario")
admin.site.register(Mascota,MascotaAdmin)

class MascotaServAdmin(admin.ModelAdmin):
    list_display=("codigo","id_servicio","id_mascota","fecha_servicio")
admin.site.register(MascotaServicio,MascotaServAdmin)

class ServicioAdmin(admin.ModelAdmin):
    list_display=("id_servi","nom","descripcion","precio","imagen")
admin.site.register(Servicio,ServicioAdmin)

class ProductoAdmin(admin.ModelAdmin):
    #DESPLEGA LOS DATOS DE LA TABLA
    list_display=("id_pro","nom_pro","desc_pro","precio_pro","foto","stock")
admin.site.register(Producto,ProductoAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id_persona","user","pas","nom","ape","dir","tel","correo","tipo","foto")
admin.site.register(Usuario,UsuarioAdmin)

class ProductoUsuarioAdmin(admin.ModelAdmin):
    list_display= ("codpu","id_persona","id_pro","cant","total")
admin.site.register(ProductoUsuario,ProductoUsuarioAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nom","FCreacion")
admin.site.register(Categoria,CategoriaAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display= ("titulo","contenido","fecha","imagen","Fcreacion","Fedicion",)
    ordering=('titulo','fecha')
    list_filter = ('id_persona_id__nom','titulo')
admin.site.register(Post,BlogAdmin)

class ContactoAdmin(admin.ModelAdmin):
    list_display=("nombre","correo","asunto","mensaje")
admin.site.register(Contacto,ContactoAdmin)