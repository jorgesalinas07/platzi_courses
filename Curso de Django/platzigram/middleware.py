"""Plazigram middleware catalog"""
#Se crea un middleware para definir un minimo de datos que debe tener el usuario
#Para poder acceder a los posts. Sino los tiene, se regresa a la pagina para agregarlos

#Importar redirect para enviar al usuario a update_profile en el caso en que le falte los
#Archivos necesarios como picture
from django.http import response
from django.shortcuts import redirect
#Importar modulo para usar reverse para validar que el usuario se encuentra en una url destinada
from django.urls import reverse

#from users.views import update_profile

#Se debe instalar el middleware en settings para poder usarlo

#Seguir la estructura de como crear un middleware con clase desde la documentación
#https://docs.djangoproject.com/en/2.0/topics/http/middleware/
class ProfileCompletionMiddleware:
    """Profile completion middleware.
    Ensure every user that is interacting with the platform
    have their profile and biography.
    """
    def __init__(self, get_response):
        """Moddleware initialization."""
        self.get_response = get_response
    
    def __call__(self, request):
        """Code to be executed for each request before the views are called"""
        #Validar que no estemos en caso anonimo (caso en el que no se ha iniciado sessión)
        if not request.user.is_anonymous:
            #Validar el caso en el que queremos entrar a admin (staff = True)
            if not request.user.is_staff:
                #Traer objeto profile
                profile=request.user.profile
                #Validar que profile en cuestion tenga tanto foto como biografia
                #Sino tiene alguna de las dos, se redirecciona al usario a update_profile para que lo agrege
                if not profile.picture or not profile.biography:
                    #Además, se realiza otra validación para que este if no se realice al infinito
                    #Esto porque cada vez que redireccione a la pagina, volverá a tener el error porque aún 
                    # no se ha agregado la info necesaria al perfil.
                    #Hay que importar reverse para hacer esto. Este se encarga de validad que el usuario se encuentra en una pagina deseada
                    #Los urls que si se pueden usar para este caso son update_profile (para agregar la info necesaria) y logout (para no agregar la info y salir del usuario) 
                    if request.path not in [reverse('users:update_profile'), reverse('users:logout')]:  
                        return redirect('users:update_profile')
          
        #Si el usuario si esta actualizado con toda la información se que necesita
        #No se hace nada y solo se responde con mismo estado (Situación) que la solicitud
        response=self.get_response(request)
        return response

