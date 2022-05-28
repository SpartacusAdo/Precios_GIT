from django.db import models
from django.contrib.auth.models import User   # Build relation user-customer  OneToOneField

class Cliente(models.Model):
    nombre=models.CharField(max_length=40)
    rut=models.IntegerField(default=0)
    dv=models.CharField(max_length=1)
    direccion=models.CharField(max_length=40)
    comuna=models.CharField(max_length=15)
    ciudad=models.CharField(max_length=15)
    pais=models.CharField(max_length=15)
    fono=models.IntegerField(default=0)
    creado_en=models.DateField(auto_now_add=True)
    modificado_en=models.DateField(auto_now=True)
    usuario=models.OneToOneField(User, related_name='cliente', on_delete=models.CASCADE)
    #lista=models.ForeignKey(Lista, related_name='listacliente', on_delete=models.CASCADE)

    class Meta:
        ordering=['nombre']

    def __str__(self):
        return self.nombre