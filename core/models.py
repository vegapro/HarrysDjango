from secrets import choice
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Categoria(models.Model):
    #id -- > numero autoincrementable , Django lo hace por nosotros
    nombre = models.CharField(max_length=80)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    valor = models.IntegerField()
    anio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=CASCADE)
    descripcion = models.TextField(null=True, blank=True)  
    stock = models.IntegerField(default=5)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return f'{self.nombre} -> {self.valor}'

opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "agradecimiento"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre


