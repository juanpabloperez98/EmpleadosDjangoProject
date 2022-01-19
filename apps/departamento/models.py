from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField(
        'Nombre', 
        max_length=50,
        blank=True
    )
    shor_name = models.CharField(
        'Nombre corto', 
        max_length=50,
        unique=True
    )
    anulate = models.BooleanField(
        'Anulado',
        default=False,
        editable=False
    )

    class Meta:
        verbose_name = 'Mi departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['-name']
        unique_together = ('name', 'shor_name')

    def __str__(self):
        return f'{self.id} - {self.name} - {self.shor_name}'