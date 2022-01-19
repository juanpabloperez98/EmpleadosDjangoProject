from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from apps.persona import models

# Listar los empleados

class ListAllEmpleados(ListView):
    # model = models.Empleado
    paginate_by = 3
    ordering = 'first_name'
    template_name = "persona/list_all.html"
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword","")
        if palabra_clave:
            lista = models.Empleado.objects.filter(
                Q(first_name__icontains = palabra_clave) | 
                Q(last_name__icontains = palabra_clave)
            )
        else:
            lista = models.Empleado.objects.all()
        return lista


class ListEmpleadosAdmin(ListView):
    # model = models.Empleado
    paginate_by = 10
    ordering = 'id'
    template_name = "persona/lista_empleados.html"
    context_object_name = 'empleados'
    model = models.Empleado

# Listar los empleados por area
class ListByAreaEmpleado(ListView):
    template_name = "persona/list_by_area.html"
    context_object_name = 'empleados'
    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = models.Empleado.objects.filter(
            departamento__shor_name = area
        )
        return lista

# Listar los empleados por palabra clave

class ListEmpleadosByKwordListView(ListView):
    """ Lista empleados por palabra clave """
    template_name = "persona/by_kword.html"
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword","")
        print("*************LLEGA")
        lista = models.Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista

# Listar habilidades de un empleado

class ListHabilidadesView(ListView):
    template_name = "persona/habilidades.html"
    context_object_name = "habilidades"

    def get_queryset(self):
        empleado = models.Empleado.objects.get(id=6)
        return empleado.Habilidades.all()


class EmpleadoDetailView(DetailView):
    model = models.Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context



class SuccessTemplateView(TemplateView):
    template_name = "persona/success.html"



class EmpleadoCreateView(CreateView):
    model = models.Empleado
    template_name = "persona/add.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'Habilidades',
        'avatar'
    ]
    # fields = ('__all__')
    success_url = reverse_lazy('persona_app:lista_empleados_admin')

    def form_valid(self, form):
        print("ENTRA")
        empleado = form.save(commit = False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super().form_valid(form)


# Actualizar un empleado
class EmpleadoUpdateView(UpdateView):
    model = models.Empleado
    template_name = "persona/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'Habilidades'
    ]
    success_url = reverse_lazy('persona_app:lista_empleados_admin')

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        print("*********METHOD POST**************")
        print(request.POST)
        return super().post(request,*args,**kwargs)

    def form_valid(self, form):
        print("*********METHOD FORM VALUE**************")
        print("***********************")
        return super().form_valid(form)



# Eliminar 
class EmpleadoDeleteView(DeleteView):
    model = models.Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:lista_empleados_admin')



class InicioView(TemplateView):
    """ Vista que carga la pagina de inicio """
    template_name = "inicio.html"




