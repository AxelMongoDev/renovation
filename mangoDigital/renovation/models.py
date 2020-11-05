from django.db import models

# Create your models here.
class BussinessContact(models.Model):
    businessName = models.CharField(max_length=25, blank=True, null=True,verbose_name="Nombre del negocio")
    businessPhone = models.CharField(max_length=25, verbose_name="Teléfono", blank=True, null=True)
    businessEmail = models.EmailField(max_length=100, verbose_name="Correo")
    businessComment = models.TextField(max_length=100,verbose_name="Comentario",  blank=True, null=True) 
    date = models.DateTimeField(auto_now_add=True,verbose_name="Fecha")
    
    def __str__(self):
        return 'Negocio:' + self.businessName