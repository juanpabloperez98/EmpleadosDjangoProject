from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import (
    ListView
)
from .forms import NewDepartamentoForm
from apps.persona.models import Empleado
from .models import Departamento
# Create your views here.



class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = "departamentos"


class NewDepartamento(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'


    def form_valid(self, form):
        dep = Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shorname']
        )
        dep.save()
        data = {
            'first_name': form.cleaned_data['nombre'],
            'last_name':form.cleaned_data['apellidos'],
            'job':'1',
            'departamento':dep
        }
        Empleado.objects.create(**data)
        return super().form_valid(form)



