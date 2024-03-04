from django.contrib import admin

# Register your models here.
# En gestion/admin.py
from django.contrib import admin
from .models import Deporte, Instalacion, Equipo, Jugador, Partido

admin.site.register(Deporte)
admin.site.register(Instalacion)
admin.site.register(Equipo)
admin.site.register(Jugador)
admin.site.register(Partido)
