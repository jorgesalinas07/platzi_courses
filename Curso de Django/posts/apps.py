'''Posts application module.'''
#Importar el modulo necesario para usar las aplicaciones
from django.apps import AppConfig


class PostsConfig(AppConfig):
    '''Posts application settings'''
    #default_auto_field = 'django.db.models.BigAutoField'
    #Darle nombre a la aplicación
    name = 'posts'
    #Darle el nombre que se mostrará de la aplicación
    verbose_name='Posts'
    