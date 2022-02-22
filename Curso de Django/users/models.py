"""User models"""

#Importar libreria para usar auth de django
from django.contrib.auth.models import User
#Importar los modelos
from django.db import models

#Usar el método de auth de proxy para autenticar datos de usuario
#models.Model es la manera de llamar a este auth (revisar documentación)
#Esta clase agrega unos campos adicionales a los que agregar auth por defecto
class Profile(models.Model):
    """Profile model.
    Proxy model that extends the base data with other
    information.
    """
    #Definir  un campo de la bdd que reciba un valor unico para que no se repitand los usuarios
    #Los valores que recibe la referencia OneToOneField son:
    #Primero a quien va a tomar, en este caso: User,
    #on_delete es el comportamiento que tiene la aplicacion cuando el objeto tomado sea detectado (Ej: cascade, protect...)
    #Revisar documentación: https://docs.djangoproject.com/en/2.0/ref/models/fields/
    #En este caso, se usa cascade para borrar los archivos relacionados con el elemento eliminado
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #Crear los demas elementos del usuario
    #models.URLField es como char pero valida que el url sea real
    website=models.URLField(max_length=200,blank=True)
    biography=models.TextField(blank=True)
    phone_number=models.CharField(max_length=20,blank=True)
    #En upload_to="" debe ir la ubicación de las fotos
    picture=models.ImageField(upload_to='users/pictures',blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    #Crear método para mostrar algún valor cuando se haga una busqueda
    def __str__(self):
        """Return Username"""
        return self.user.username
