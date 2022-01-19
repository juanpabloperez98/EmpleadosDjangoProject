from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView

from .models import Prueba
from .forms import PruebaForm

# Create your views here.
class PruevaVIEW(TemplateView):
    template_name = "home/prueba.html"

class ResumeFoundationVIEW(TemplateView):
    template_name = "home/resume_foundation.html"


class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = "listaNums"
    queryset = ['1','2','3']


class ListarPruebasView(ListView):
    template_name = "home/listar_prueba.html"
    model = Prueba
    context_object_name = "listaPrueba"


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/'
