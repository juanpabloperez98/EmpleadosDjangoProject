from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path('listar_empledos/', views.ListAllEmpleados.as_view(), name="empleados_all"),
    path('listar_by_area/<shorname>/', views.ListByAreaEmpleado.as_view(),name="empleados_area"),
    path('listar_empleados_admin/', views.ListEmpleadosAdmin.as_view(),name="lista_empleados_admin"),
    path('buscar-empleado/', views.ListEmpleadosByKwordListView.as_view()),
    path('listar_habilidades/', views.ListHabilidadesView.as_view()),
    # Details View
    path('ver-empleado/<pk>', views.EmpleadoDetailView.as_view(), name="empleado_detail"),
    # Create View
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name="empleado_add"),
    # Template View
    path('success/', views.SuccessTemplateView.as_view(), name="success"),
    # Update View
    path('update-empleado/<pk>', views.EmpleadoUpdateView.as_view(), name="update-empleado"),
    # Delete View
    path('delete-empleado/<pk>', views.EmpleadoDeleteView.as_view(), name="delete-empleado"),
    path('', views.InicioView.as_view(), name="inicio"),
]
