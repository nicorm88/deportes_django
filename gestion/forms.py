from django import forms
from .models import Deporte, Instalacion, Equipo, Jugador, Partido

class DeporteForm(forms.ModelForm):
    class Meta:
        model = Deporte
        fields = ['nombre'] 


class InstalacionForm(forms.ModelForm):
    class Meta:
        model = Instalacion
        fields = ['nombre', 'direccion', 'iluminacion', 'cubierta']


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'deporte', 'descripcion_equipaciones', 'nombre_contacto', 'telefono_contacto', 'correo_contacto']


class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'apellidos', 'equipo', 'dorsal', 'fecha_nacimiento', 'altura', 'peso', 'telefono_contacto']


class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ['fecha_hora', 'deporte', 'instalacion', 'equipo_local', 'equipo_visitante', 'puntos_local', 'puntos_visitante', 'observaciones']