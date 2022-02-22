#Borrar todo porque todo se puede hacer con libreria authentication
#Importar librerira para registrar una url con los administradores del servidor
from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path
#Importar modulo donde se va a desarrollar la vista hello_world
from platzigram import views
#Libreria adicional para poder mostrar fotos en la pagína
from django.conf.urls.static import static
#Para usar la libreria de mostrar fotos se necesita settings:
from django.conf import settings
#Agregar un "as" en la importación para diferenciar las importaciones que vienen de
#Aplicaciones locales de django y las que son creadas
from platzigram import views as local_views
#Importar modelo para la vista de posts
from posts import views as post_views
#Importar modelo para la vista del login del usuario
from users import views as users_views
#Importar include para poder enviar url a otros lugares y llamarlas desde allá
from django.urls import path, include

#Modulo para escribir una respuesta http
# from django.http import HttpResponse

# def hello_world(request):
#     return HttpResponse('Hello, world!')

#Los paths funcionan definiendo la url a la cuál se desea responder algo
urlpatterns = [
    #Borrar todo porque todo se puede hacer con libreria authentication
    # #Especificar que la vista esta ubicada en el modulo views con nombre hello_world
    # path('hello-world/', local_views.hello_world),
    # path('hi/', local_views.hi),
    # path('sort/', local_views.sort),
    # #Crear url para validad que el usuario es mayor de 15 años
    # #La segunda cosa que agrega django son los argumentos requeridos
    # #En este caso, se declaró que se requerián las variables name y age así estás se pasan
    # path('hi/<str:name>/<int:age>/', local_views.say_hi),
    # #Vista para imprimir todas las urls de admin
    path('admin/', admin.site.urls),
    #Se inicia un include para mover urls y tener mas organización
    #Este recibe una tupla (indica donde esta el modulo y de que app viene) 
    # y un namespace que es un conjunto de nombres    
    #En la tupla tiene dos elementos: 1.) modulo de urls 2.) Nombre de la applicación
    #El primer argumento es la ruta. Para el caso de posts se empieza a escribir desde la raíz así que se deja en blanco
    path('', include(('posts.urls','posts'),namespace='posts')),
    #La ruta es users, el nombre del modulo es urls y el nombre de la app es users
    path('users/', include(('users.urls','users'),namespace="users")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
#Además, se debe crear un archivo MEDIA_URL en settigs para que se tomen las imagenes
#Mas información en: https://docs.djangoproject.com/en/2.0/ref/settings/#media-root
