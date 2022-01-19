from django.contrib import admin
from .models import Empleado, Habilidades
from django.contrib import admin
# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name'
    )
    search_fields = ('first_name',)
    list_filter = ('job',)
    def full_name(self,obj):
        return f"{obj.first_name} {obj.last_name}"
    filter_horizontal = ('Habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)