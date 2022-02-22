"""Posts models."""

#Django
# from django.db import models

# class User(models.Model):
#     """User model"""
#     #Definir los miembros de la tabla usando ORM
#     #Agregar algunos tags que se pueden encontrar en la documentación
    
#     #Que el email sea único
#     email=models.EmailField(unique=True)
#     #Que los Char tengan maximo 100 caracteres
#     password=models.CharField(max_length=100)
#     first_name=models.CharField(max_length=100)
#     last_name=models.CharField(max_length=100)
#     #Que se pueda poner o no el bio
#     bio = models.TextField(blank=True)
#     #Que se pueda o no colocar la fecha
#     birthdate = models.DateField(blank=True, null=True)
#     #Que se cree la fecha inmediatamente se crea la variable
#     created=models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)
#     #Verificar si el usuario que esta registrado es admin o no con un boolean
#     #Se define por defecto en False para que no cualquiera sea admin
#     is_admin=models.BooleanField(default=False)
#     country=models.CharField(max_length=50, default="Colombia")
#     city=models.CharField(max_length=50, default="barranquilla")

#     #Crear método para cuando se usa filter. 
#     # Esto para que se muestre un string en lugar del id
#     #Esto lo hará para cualquier filter echo (?)
#     def __str__(self):
#         """Return email."""
#         return self.email 


#Libreria de django para crear modelos
from django.db import models
#Importar user para poder usar foreigh key
from django.contrib.auth.models import User

# #Crear el modelo de posts con todos los datos necesarios que no sea de usuario
# #Porque esos estan guardados en auth
class Post(models.Model):
    """Post model."""
    #Usar foreigh key para relacionar el usuario creado en auth
    #Se coloca CASCADE en on_delete para que se borren todos los posts cuando se borre el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    #Hacer funcion para mostrar algunos valores cuando se hace un filtro
    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.user.username)
