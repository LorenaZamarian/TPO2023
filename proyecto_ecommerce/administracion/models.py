from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
 


# Create your models here.

class Bodega(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    # campo del tipo slug
    nombre_slug = models.SlugField(max_length=100,verbose_name='Nombre Slug')
    ubicacion = models.CharField(max_length=50,verbose_name='Ubicacion')
    telefono = models.CharField(max_length=20,verbose_name='Telefono')
    email = models.EmailField(max_length=150,null=True)
    baja = models.BooleanField(default=0)

    def __str__(self):
        return self.nombre

    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()

class Varietal(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    # campo del tipo slug
    nombre_slug = models.SlugField(max_length=100,verbose_name='Nombre Slug')
    descripcion = models.TextField(null=True,verbose_name='Descripcion')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural='Varietales'

class Producto(models.Model):
    nombre = models.CharField(max_length=250,verbose_name='Nombre')
    # campo del tipo slug
    nombre_slug = models.SlugField(max_length=100,verbose_name='Nombre Slug')
    precio = models.DecimalField(max_digits=15,decimal_places=2,default=0.0,verbose_name='Precio')
    stock = models.CharField(max_length=10,verbose_name='Stock')
    imagen = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Imagen')
    bodega = models.ForeignKey(Bodega,on_delete=models.CASCADE) # relacion mucho a uno
    varietal = models.ForeignKey(Varietal,on_delete=models.CASCADE)  # relacion mucho a uno
    cosecha = models.CharField(max_length=10,verbose_name='Cosecha',null=True)
    descripcion = models.TextField(null=True,verbose_name='Descripcion')
    activo=models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    def delete(self,using=None,keep_parents=False):
        self.imagen.storage.delete(self.imagen.name) #borrado fisico
        super().delete()
    
    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super().save(*args, **kwargs)

        

class Detalle_venta(models.Model):
    Producto = models.ForeignKey(Producto,on_delete=models.CASCADE) # relacion mucho a uno
    nombre_slug = models.SlugField(max_length=100,verbose_name='Nombre Slug')
    cantidad = models.IntegerField(default=0,verbose_name='Cantidad')
    precio = models.DecimalField(max_digits=15,decimal_places=2,default=0.0,verbose_name='Precio')
  
    def __str__(self):
        return self.nombre

    def delete(self,using=None,keep_parents=False):
        self.imagen.storage.delete(self.imagen.name) #borrado fisico
        super().delete()
    
    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super().save(*args, **kwargs)

class Venta(models.Model):
    nombre_slug = models.SlugField(max_length=100,verbose_name='Nombre Slug')
    num_comprobante = models.IntegerField(default=0,verbose_name='Numero comprobante')
    fecha_venta = models.DateField(auto_now_add=True,verbose_name='Fecha')
    total_venta = models.DecimalField(max_digits=15,decimal_places=2,default=0.0,verbose_name='Total')
    Detalle_venta = models.ForeignKey(Detalle_venta,on_delete=models.CASCADE, default=0)
  

    def __str__(self):
        return self.nombre

    def delete(self,using=None,keep_parents=False):
        self.imagen.storage.delete(self.imagen.name) #borrado fisico
        super().delete()
    
    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super().save(*args, **kwargs)



class PersonaAbs(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=150,verbose_name='Apellido')
    email = models.EmailField(max_length=150,null=True)
    dni = models.IntegerField(verbose_name="DNI")
    telefono = models.IntegerField(verbose_name="Telefono")
    domicilio = models.CharField(max_length=150,verbose_name='Domicilio')
    nombre_usuario = models.CharField(max_length=150,verbose_name='Nombre de usuario')
    cotraseña = models.CharField(max_length=150,verbose_name='Contraseña')
    is_superuser = models.BooleanField(verbose_name= 'Superuser')
    is_staff = models.BooleanField (verbose_name='Staff')
    is_active = models.BooleanField(verbose_name='Activo')

    class Meta:
        abstract=True

class ClienteAbs(PersonaAbs):
    baja = models.BooleanField(default=0,null=True)
    #relacion many to many
    ventas = models.ManyToManyField(Venta)

    def __str__(self):
        return self.nombre

    def delete(self,using=None,keep_parents=False):
        self.imagen.storage.delete(self.imagen.name) #borrado fisico
        super().delete()
    
    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super().save(*args, **kwargs)

class MiembroAbs(PersonaAbs):
    legajo = models.CharField(max_length=10,verbose_name='Legajo')

    def __str__(self):
        return self.nombre

    def delete(self,using=None,keep_parents=False):
        self.imagen.storage.delete(self.imagen.name) #borrado fisico
        super().delete()
    
    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super().save(*args, **kwargs)

#MODELO DE USARIO DE DJANGO
"""
class Usuario(AbstractUser):
    pass

class Perfil(models.Model):
    #MODELO QUE PERMITE DEL USER MODEL DE DJANGO PARA AGREGERLE CAMPOS EXTRAS
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE,primary_key=True)
    telefono = models.CharField(max_length=20,verbose_name='Teléfono')
    domicilio = models.CharField(max_length=20,verbose_name='Domicilio')
    foto = models.ImageField(upload_to='perfiles/',null=True,verbose_name='Foto Perfil')
"""    