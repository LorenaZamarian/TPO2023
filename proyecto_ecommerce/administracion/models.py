from django.db import models

# Create your models here.
class Bodega(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
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
    descripcion = models.TextField(null=True,verbose_name='Descripcion')
    baja = models.BooleanField(default=0)

    def __str__(self):
        return self.nombre

    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()

#Modelo UNICO - SOLUCION 1
class Producto(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    precio = models.FloatField(max_length=6,verbose_name='Precio')
    stock = models.CharField(max_length=10,verbose_name='Stock',null=True)
    imagen = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Imagen')
    bodega = models.ForeignKey(Bodega,on_delete=models.RESTRICT)
    varietal = models.ForeignKey(Varietal,on_delete=models.RESTRICT)
    cosecha = models.CharField(max_length=10,verbose_name='Cosecha',null=True)
            