from django.db import models

# Create your models here.
#python manage.py createsuperuser
class Troll(models.Model):
    ApellidoPaterno= models.CharField(max_length=35)
    ApellidoMaterno= models.CharField(max_length=35)
    Nombres= models.CharField(max_length=35)
    RUT= models.CharField(max_length=8)
    FechaNacimiento = models.DateField()
    SEXOS=(('F','Femenino'),('M','Masculino'))
    Sexo=models.CharField(max_length=1,choices=SEXOS,default='M')
    image = models.BinaryField(blank=True)

    def NombreCompleto(self):
        cadena= "{0} {1},{2}"
        return cadena.format(self.ApellidoPaterno,self.ApellidoMaterno,self.Nombres)
    
    def __str__(self):
        return self.NombreCompleto()

    