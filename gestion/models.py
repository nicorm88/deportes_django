from django.db import models

# Create your models here.
from django.db import models

class Deporte(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Instalacion(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    iluminacion = models.BooleanField(default=False)
    cubierta = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    descripcion_equipaciones = models.TextField()
    nombre_contacto = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=15)
    correo_contacto = models.EmailField()

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    dorsal = models.PositiveIntegerField()
    fecha_nacimiento = models.DateField()
    altura = models.FloatField()
    peso = models.FloatField()
    telefono_contacto = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Partido(models.Model):
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    instalacion = models.ForeignKey(Instalacion, on_delete=models.CASCADE)
    equipo_local = models.ForeignKey(Equipo, related_name='equipo_local', on_delete=models.CASCADE)
    equipo_visitante = models.ForeignKey(Equipo, related_name='equipo_visitante', on_delete=models.CASCADE)
    puntos_local = models.PositiveIntegerField()
    puntos_visitante = models.PositiveIntegerField()
    observaciones = models.TextField()
 