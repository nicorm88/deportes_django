from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Deporte, Instalacion, Equipo, Jugador, Partido
from gestion.forms import DeporteForm, InstalacionForm, EquipoForm, JugadorForm
from django.urls import reverse_lazy

class IndexView(ListView):
    model = Partido
    template_name = 'index.html'
    context_object_name = 'ultimos_partidos'

    def get_queryset(self):
        return Partido.objects.order_by('-fecha_hora')[:5]

class DeportesListView(ListView):
    model = Deporte
    template_name = 'listar_deportes.html'
    context_object_name = 'deportes'

class DeporteCreateView(CreateView):
    model = Deporte
    form_class = DeporteForm
    template_name = 'agregar_deporte.html'
    success_url = reverse_lazy('deportes')

class DeporteUpdateView(UpdateView):
    model = Deporte
    form_class = DeporteForm
    template_name = 'modificar_deporte.html'
    success_url = reverse_lazy('deportes')

class DeporteDeleteView(DeleteView):
    model = Deporte
    template_name = 'confirmar_borrar_deporte.html'
    success_url = reverse_lazy('deportes')


class InstalacionesListView(ListView):
    model = Instalacion
    template_name = 'listar_instalaciones.html'
    context_object_name = 'instalaciones'

class InstalacionCreateView(CreateView):
    model = Instalacion
    form_class = InstalacionForm
    template_name = 'agregar_instalacion.html'
    success_url = reverse_lazy('instalaciones')

class InstalacionUpdateView(UpdateView):
    model = Instalacion
    form_class = InstalacionForm
    template_name = 'modificar_instalacion.html'
    success_url = reverse_lazy('instalaciones')

class InstalacionDeleteView(DeleteView):
    model = Instalacion
    template_name = 'confirmar_borrar_instalacion.html'
    success_url = reverse_lazy('instalaciones')

class EquiposListView(ListView):
    model = Equipo
    template_name = 'listar_equipos.html'
    context_object_name = 'equipos'

class EquipoDetailView(DetailView):
    model = Equipo
    template_name = 'detalle_equipo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        equipo = self.get_object()
        context['jugadores'] = Jugador.objects.filter(equipo=equipo)
        return context

class EquipoCreateView(CreateView):
    model = Equipo
    form_class = EquipoForm
    template_name = 'agregar_equipo.html'
    success_url = reverse_lazy('equipos')


class EquipoUpdateView(UpdateView):
    model = Equipo
    form_class = EquipoForm
    template_name = 'modificar_equipo.html'
    success_url = reverse_lazy('equipos')

class JugadorCreateView(CreateView):
    model = Jugador
    form_class = JugadorForm
    template_name = 'agregar_jugador.html'
    success_url = reverse_lazy('equipos')

class EquipoDeleteView(DeleteView):
    model = Equipo
    template_name = 'confirmar_borrar_equipo.html'
    success_url = reverse_lazy('equipos')

class JugadoresListView(ListView):
    model = Jugador
    template_name = 'listar_jugadores.html'
    context_object_name = 'jugadores'

class JugadorDetailView(DetailView):
    model = Jugador
    template_name = 'detalle_jugador.html'

class JugadorCreateView2(CreateView):
    model = Jugador
    form_class = JugadorForm
    template_name = 'agregar_jugador2.html'
    success_url = reverse_lazy('jugadores')

class JugadorUpdateView(UpdateView):
    model = Jugador
    form_class = JugadorForm
    template_name = 'modificar_jugador.html'
    success_url = reverse_lazy('jugadores')

class JugadorDeleteView(DeleteView):
    model = Jugador
    template_name = 'confirmar_borrar_jugador.html'
    success_url = reverse_lazy('jugadores')

class PartidosListView(ListView):
    model = Partido
    template_name = 'listar_partidos.html'
    context_object_name = 'partidos'
    ordering = ['-fecha_hora']

class PartidoDetailView(DetailView):
    model = Partido
    template_name = 'detalle_partido.html'
    context_object_name = 'partido'

class PartidoCreateView(CreateView):
    model = Partido
    fields = ['fecha_hora', 'deporte', 'equipo_local', 'equipo_visitante']
    template_name = 'agregar_partido.html'
    success_url = reverse_lazy('partidos')

    def form_valid(self, form):
        if form.instance.equipo_local == form.instance.equipo_visitante:
            form.add_error(None, 'El equipo local no puede ser el mismo que el equipo visitante.')
            return super().form_invalid(form)
        return super().form_valid(form)

class PartidoUpdateView(UpdateView):
    model = Partido
    fields = ['fecha_hora', 'deporte', 'equipo_local', 'equipo_visitante']
    template_name = 'modificar_partido.html'
    success_url = reverse_lazy('partidos')

    def form_valid(self, form):
        if form.instance.equipo_local == form.instance.equipo_visitante:
            form.add_error(None, 'El equipo local no puede ser el mismo que el equipo visitante.')
            return super().form_invalid(form)
        return super().form_valid(form)

class PartidoDeleteView(DeleteView):
    model = Partido
    template_name = 'confirmar_borrar_partido.html'
    success_url = reverse_lazy('partidos')


