from django.db import models
from django.utils.text import slugify 


# Create your models here.
<<<<<<< HEAD

=======
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

        
>>>>>>> Vale
