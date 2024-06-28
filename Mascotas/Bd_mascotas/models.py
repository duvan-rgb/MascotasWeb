from django.db import models
from django.utils.timezone import now

class Mascota(models.Model):

    tipomascota = [
        ("Felino", "Felino"),
        ("Canino", "Canino"),
        ("Pajaro", "Pajaro"),
        ("Reptil", "Reptil"),
    ]

    id_mascota = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=45 ,choices=tipomascota)
    raza = models.CharField(max_length=45)
    nom_mas = models.CharField(max_length=45)
    fecha_naci = models.DateField()
    foto = models.ImageField(upload_to="Media/MascotaImg", verbose_name="Imagen")
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'mascota'

    def __str__(self):
        texto= "{0}"
        return texto.format(self.id_mascota)
    
    
class MascotaServicio(models.Model):
    codigo = models.IntegerField(primary_key=True)
    id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_servicio')
    id_mascota = models.ForeignKey(Mascota, models.DO_NOTHING, db_column='id_mascota')
    fecha_servicio = models.DateField()

    class Meta:
        managed = False
        db_table = 'mascota_servicio'

class Producto(models.Model):
    id_pro = models.AutoField(primary_key=True)
    nom_pro = models.CharField(max_length=45)
    desc_pro = models.CharField(max_length=45)
    precio_pro = models.FloatField()
    foto = models.ImageField(upload_to="Media/ProductoImg", verbose_name="Imagen")
    stock = models.FloatField()

    class Meta:
        managed = False
        db_table = 'producto'
    
    def __str__(self):
        texto= "{0}"
        return texto.format(self.id_pro)


class ProductoUsuario(models.Model):
    codpu = models.IntegerField(db_column='codPU', primary_key=True)  # Field name made lowercase.
    id_persona = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_persona')
    id_pro = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_pro')
    cant = models.FloatField()
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'producto_usuario'


class Servicio(models.Model):
    id_servi = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="Media/ServivioImg", verbose_name="Imagen")

    class Meta:
        managed = False
        db_table = 'servicio'

    def __str__(self):
        texto= "{0}"
        return texto.format(self.id_servi)
#AGREGAMOS UN DICCIONARIO CON LAS OPCIONES DEL USUARIO
op=[
    [0,"Administrador"],
    [1,"Cliente"],
]

class Usuario(models.Model):
    id_persona = models.IntegerField(primary_key=True)
    user = models.CharField(unique=True, max_length=45, blank=True, null=True)
    pas = models.CharField(max_length=45, blank=True, null=True)
    nom = models.CharField(max_length=45, blank=True, null=True)
    ape = models.CharField(max_length=45, blank=True, null=True)
    dir = models.CharField(max_length=45, blank=True, null=True)
    tel = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True, choices= op)
    foto = models.ImageField(upload_to="Media/Blogimg",blank=True, null=True, verbose_name="Imagen")

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        texto= "{0}"
        return texto.format(self.id_persona)
    
#PARA ESTOS MODELOS IMPORTAMOS LA LIBRERIA TIMEZONE
class Categoria(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nombre")
    FCreacion = models.DateTimeField(auto_now_add=True , verbose_name="Fecha de creacion")
    
    class Meta:
        verbose_name="categoria"

    def __str__(self):
        texto= "{0}"
        return texto.format(self.nom)
    
class Post(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Titulo")
    contenido = models.TextField(verbose_name="Contenido")
    fecha= models.DateTimeField (default=now , verbose_name="Fecha de publicacion")
    imagen = models.ImageField (upload_to="BlogImg", null=True, blank=True, verbose_name="Imagen")
    id_persona = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    categorias = models.ManyToManyField(Categoria, verbose_name="Categorias")
    Fcreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    Fedicion = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name="Post"

    def __str__(self):
        texto= "{0}"
        return texto.format(self.titulo)
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    correo = models.CharField(max_length=100, verbose_name="Correo")
    asunto = models.CharField(max_length=100, null=True, blank=True, verbose_name="Asunto")
    mensaje = models.CharField(max_length=500, verbose_name="Mensaje")

    class Meta:
        verbose_name="Contacto"

    