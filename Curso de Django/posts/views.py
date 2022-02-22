#Otra forma de reponse
#Render recibe un request y el nombre del template. Además, importar redirect para poder direccionar a otra url
from django.shortcuts import render, redirect
#Importar libreria para los response Http
from django.http import HttpResponse
from datetime import datetime
#Importar modulo para que solo se puede acceder a los feed si
#Se ha ingresado un usuario
from django.contrib.auth.decorators import login_required
import posts
#Forms
#Importar forms para acciones repetitivas como crear un post
from posts.forms import PostForm
#from users.models import Profile

#Importar los posts creados desde models
from posts.models import Post

#Importar modulo para hacer que una class-based view sea LoginRequired
from django.contrib.auth.mixins import LoginRequiredMixin
#Importar modulo para mostrar la lista de posts con class-based views
#Se importa #DetailView para mirar los posts individual con detalle
#Se importar CreateView para crear un posts nuevo
from django.views.generic import ListView, DetailView, CreateView
#Evaluar url hasta que lo necesite
from django.urls import reverse_lazy


#Iniciar class-bassed view para mostrar posts
#Estucura según la documentación: https://docs.djangoproject.com/en/2.0/topics/class-based-views/generic-display/#detailview
class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""
    #Definir template
    template_name='posts/feed.html'
    #Definir de modelo (de donde toma la info)
    model = Post
    #Definir el orden: en orden desendente desde que se creó
    ordering = ('-created')
    #Número de elementos a mostrar por pagina
    paginate_by = 30
    #Nombre del query en el template
    context_object_name = 'posts'

#Clase para mostrar los detalles de un post
#Seguir la estructura de la documentación con: https://docs.djangoproject.com/en/2.0/topics/class-based-views/generic-display/#detailview
class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""
    #Si no se le envía el template_name o context_object_name, esperar a que existan en una capeta predeterminada
    template_name = 'posts/detail.html'
    #Seleccionar todos los posts
    queryset= Post.objects.all()
    context_object_name='post'


#Crear un diccionario con algunos posts para mostrar
# posts=[
#     {
#         'name': 'Mont Blac',
#         'user': 'Yésica Cortés',
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'picture': 'https://picsum.photos/200/200/?image=1036',
#     },
#     {
#         'name': 'Via Láctea',
#         'user': 'C. Vander',
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'picture': 'https://picsum.photos/200/200/?image=903',
#     },
#     {
#         'name': 'Nuevo auditorio',
#         'user': 'Thespianartist',
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'picture': 'https://picsum.photos/200/200/?image=1076',
#     }
# ]

#Crear un posts con algunos datos adicionales

# posts=[
#     {
#         'title': 'Mont Blanc',
#         'user': {
#             'name': 'Yésica Cortés',
#             'picture': 'https://picsum.photos/60/60/?image=1027'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/800/600?image=1036',
#     },
#     {
#         'title': 'Via Láctea',
#         'user': {
#             'name': 'Christian Van der Henst',
#             'picture': 'https://picsum.photos/60/60/?image=1005'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/800/800/?image=903',
#     },
#     {
#         'title': 'Nuevo auditorio',
#         'user': {
#             'name': 'Uriel (thespianartist)',
#             'picture': 'https://picsum.photos/60/60/?image=883'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/500/700/?image=1076',
#     }
# ]

#Función para mostrar los posts echos usando httpresponse
# def list_posts(request):
#     """List existing posts"""
#     content=[]
#     #Crear for para ir mostrando todos los valores del diccionario
#     for post in posts:
#         content.append("""
#             <p><strong>{name}</strong></p>
#             <p><small>{user} - <i>{timestamp}</i></small></p>
#             <figure><img src="{picture}"/></figure>
#         """.format(**post))
#         #Se coloca el **post para que tome cualquier tamaño de llaves y valores de diccionario
#     return HttpResponse('<br>'.join(content))
#         #La etiqueta '<br>' se encarga de poner espacios
#         #join() sirve para unir todo en un solo string
    
#Decorador para que solo se vean la lista de posts si hay un login registrado
#Para esto también se debe colocar en LOGIN_URL en settings y importar el modulo necesario
#Para mas información: https://docs.djangoproject.com/en/2.0/topics/auth/default/#authentication-in-web-requests
# @login_required
#Se cambió para hacer lo mismo con class-based views

# def list_posts(request):
#     """List exiting posts"""
#     #render busca templates. Ubica el template solo con el nombre porque la 'APP_DIRS' esta True en settings
#     #Para que esto ocurra, debe haberse creado el folder "template" dentro de la app con este nombre
#     #Como ultimo parametro, este recibe es un contexto (diccionario)
#     #A continuación, mostramos el contenido de la variable name (Jorge) por medio de render
#     # return render(request, 'feed.html', {'name':'Jorge'})

#     #Ahora mostraremos los posts con ese nombre
#     #return render(request, 'posts/feed.html', {"posts":posts})

#     #Ahora se tomarán los posts reales creados por los usuario!!
#     #Objects.all() toma todos los valores
#     #se ordenan en orden desendente al creado
#     posts = Post.objects.all().order_by('-created')
#     return render(request, 'posts/feed.html', {"posts":posts})


#Remplazar una función común y repetitiva (crear un post) por una class-based view
#Se hace utilizando el generic de documentación: http://ccbv.co.uk/projects/Django/2.0/django.views.generic.edit/CreateView/
#Además, de usa la estructura de una clase con los mixing: https://docs.djangoproject.com/en/2.0/topics/class-based-views/generic-display/#detailview
#Estructura y ejemplo de createview: https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView
class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""
    template_name='posts/new.html'

    form_class=PostForm
    #Una vez se crea el porst, redireccionar a post/feed
    success_url= reverse_lazy('posts:feed')

    #Agregar contexto
    def get_context_data(self, **kwargs):
        #Tomar todos los valores de la publicación escritos por el usuario
        context= super().get_context_data(**kwargs)
        #Agregar llave a context que sea user y guarde la info de user
        context['user']=self.request.user
        #Agregar llave a context que sea profile y guarde la info de profile
        context['profile']=self.request.user.profile
        return context

# #Crear post con método funciones
# #Usar form para accion repetitiva de crear post
# #Asegurarse de que solo se pueda crear un post si hay una session iniciada
# @login_required
# def create_post(request):
#     """Create a new posts"""
#     if request.method=='POST':
#         #Seguir la estructura de la documentación de un form: https://docs.djangoproject.com/en/2.0/topics/forms/
#         #Crear variable que reciba los datos echos por la clase PostForm al
#         #Recibir los datos escribo por el usuario en la solicitud (tanto escritos como imagenes)
#         form = PostForm(request.POST, request.FILES)
#         #Si es valido se guarda el post y redirige al feed
#         if form.is_valid():
#             form.save()
#             return redirect('posts:feed')
    
#     else:
#         form = PostForm()
    
#     #Si no entra en ningún if es porque no se esta crando un usuario así que se devuelve toda la información igual
#     #Context es lo que necesita el form para funcinar
#     return render(
#         request=request,
#         template_name='posts/new.html',
#         context={
#             'form': form,
#             'user':request.user,
#             'profile': request.user.profile
#         }
#         )