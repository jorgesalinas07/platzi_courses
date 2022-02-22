"""Users views"""

#Django
#Modulo para usar templates
#Importar redirect para hacer redirecciones en la pagína
# from django import db
# from django.db.models.fields import PositiveIntegerRelDbTypeMixin
from django.shortcuts import render, redirect
#Modulo para hacer login
from django.contrib.auth import authenticate, login
#Modulo para hacer logout
from django.contrib.auth import logout
#Importar modulo para no se trate de hacer logout de usa session inexistente
from django.contrib.auth.decorators import login_required
#Importar modulo para crear un usuario nuevo
from django.contrib.auth.models import User
from django.urls.base import reverse_lazy

#Importar Profile para poder agregar un perfil nuevo una vez se cree un usuario
#También para poder actualizar el perfil con cambios
from users.models import Profile
#Exception
#Importar un tipo en especifico de exception para el caso en el que se crea un usuario con el mismo nombre que otro y creado
#Esto se hace para validad que en realidad este es el error elevado que esta ocurriendo y no otro
# from django.db.utils import IntegrityError

#Importar modulo forms para hacer trabajos repetitivos
from users.forms import SignupForm

#Importar libreria para poder crear una url y usala para redireccionar
#Esto porque redirect no puede redireccionar a una url que necesite argumentos 
#Revese se encarga de construir una url
from django.urls import reverse

#Importar posts para poder mostrar los posts echos por los usuarios
from posts.models import Post 


#Importar modulo para usar vistas basadas en clases
#Importar modulo para FormView, una vista basada en clases para el signup 
#Import update view para hace update_profile
from django.views.generic import DetailView, FormView, UpdateView
#Importar modulo para hacer que una class-based view sea LoginRequired
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import views as auth_views


 

#Empezar a definir la clase para usar vistas basadas en clases
#Se usa un mixin para hace que login required con class-based views
class UserDetailView(LoginRequiredMixin, DetailView):
    """Class-based view show a profile data"""
    #Llamar la ubicación del template
    template_name = 'users/detail.html/'
    #Traer los datos del perfil que se va a mostrar.
    #Definir slug (campo de texto unico) para que se ubique al usuario que se desea mostrar
    slug_field = 'username'
    #Además, se define otra variable necesaria para la ubicación. El 'username' es así porque
    #En los views.urls se definió que el str usado se llama username. Debe tener el mismo nombre de str 
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    #Nos aseguramos que el objeto que venga desde detail.html sea de nombre 'user' (como se definió en el .html)
    #Esto para garantizar que todo esta en orden
    context_object_name='user'

    #Se procede a agregar la lista de posts que el usuario a echo
    #Para esto se sigue la documentación de añadir información a un class-based view
    #https://docs.djangoproject.com/en/2.0/topics/class-based-views/generic-display/#detailview
    
    def get_context_data(self, **kwargs):
        """ Add user's posts to context"""
        #Traer la información de cualquier tipo y tamaño con get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        #En la variable user se guarda el usuario en cuestion
        user= self.get_object()
        #Ahora se hace un query para tomar los objetos (posts) tomados del usuario y ordenarnos del ultimo al primero
        context['posts'] = Post.objects.filter(user=user).order_by('-created')

        return context


#Usar login con class-based views con método de django
#Se debe importar modulo de django para que funcione from django.contrib.auth import views as auth_views
#Seguir la estructura de la documentación: https://docs.djangoproject.com/en/2.0/topics/auth/default/#module-django.contrib.auth.views
class LoginView(auth_views.LoginView):
    """Login view."""
    template_name='users/login.html'


#Hacer log in con función
# def login_view(request):
#     """Login view."""
#     #Inicia debugger para poder revisar los usuarios y contraseñas de los usuarios
#     #import pdb; pdb.set_trace()
#     #Solo se hace para verificar que solo se tome el usuario cuando se realice una petición de tipo POSTS
#     #Esto por que eso significa que se esta intentando escribir el usuario y contraseña
#     #Para mas información en la documentación: https://docs.djangoproject.com/en/2.0/topics/auth/default/#authentication-in-web-requests
#     if request.method=='POST':
#         #Crear variables de la documentación para recibir el usuario y contraseña
#         username=request.POST['username']
#         password=request.POST['password']
#         #Usar el comando autenticate para verificar si hace match con algún usuario existente
#         user = authenticate(request, username=username, password=password)
#         #Si devuelve un resultado positivo, usar comando login
#         #Sino, devolver la info que el usuario escribió
#         if user:
#             login(request, user)
#             # Usar redireccion para evitar que se vuelva a cometer un error por el usuario
#             return redirect('posts:feed')
#         else:
#             return render(request, 'users/login.html', {'error': 'Invalid username and password'})

#     return render(request, 'users/login.html')


#Hacer signup con class-based views
class SignupView(FormView):
    """User detail view."""
    #Seguir la estructura de la documentación de un FormView
    #https://ccbv.co.uk/projects/Django/2.0/django.views.generic.edit/FormView/
    #https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView
    template_name='users/signup.html'
    form_class=SignupForm
    success_url = reverse_lazy('users:login')
    #Validar el form y si es correcto, guardar los datos
    
    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)


# #Función para crear un perfil
# def signup(request):
#     """Sign up view"""
#     #Para comprobar que esta funcionando lo valores pedidos en el template signup (usename, email...) se usa el debuger
#     #Ahí se usan el comando request.POST (POST es el método usado para escribir los datos) antes y después de escribir los datos para revisar si los tomó
#     #import pdb; pdb.set_trace()
#     #Una vez validado que si se esta recibiendo los datos con el método POST se reciben estos valores
#     # if request.method=="POST":
#     #     #request.POST[""] es la manera de recibir un valor de request con el método POST
#     #     username=request.POST['username']
#     #     passwd=request.POST["passwd"]
#     #     passwd_confirmation=request.POST['passwd_confirmation']
#     #     #Se realiza una confirmación del password usando estas dos ultimas variables

#     #     if passwd != passwd_confirmation:
#     #         #Si detecta que no son iguales, se enviará un mensaje de error al template signup.html
#     #         #En el archivo signup.html debe haber un código que reciba el error 
#     #         return render(request, "users/signup.html", {'error': 'Password confirmation does not match'})
        
#     #     #Se debe validar el caso para el cuál se intente agregar un usuario que ya esta registrado en la base de datos
#     #     #Si esto ocurre, django elevará un error de "UNIQUE constraint failed: auth_user.username"
#     #     #Para evitarlo, se usara un try - except que valide este error. Esto solo se hará para este campo
#     #     try:
#     #         #En el try se procederá a crear el usuario
#     #         #Lo indispensable para crear un usuario solo es el username y password, lo demas es opcional
#     #         #A continuación se siguen los pasos de la documentación para crear el usuario (https://docs.djangoproject.com/en/2.0/topics/auth/default/#creating-users)
#     #         user = User.objects.create_user(username=username,password=passwd)
#     #     except IntegrityError:
#     #         #En el except se validará el error. Se usará el if del template html en el que muestra el mensaje de error, el cuál esta siendo definido aquí
#     #         #El error elevado para este caso es IntegrityError. Se toma aquí para validar que en realidad ese es el error que esta ocurriendo.
#     #         # Para esto, se debe importar el error (Mirar arriba).
#     #         return render(request, 'users/signup .html', {'error': 'Username is already a user'})
#     #     #Una vez ya el usuario esta creado porque tiene lo minimo necesario para ser creado
#     #     #Se procede a agregar los datos adicionales:
#     #     user.first_name=request.POST['first_name']
#     #     user.last_name=request.POST['last_name']
#     #     user.email=request.POST['email']     
#     #     #Guardar cambios en la base de datos
#     #     user.save()

#     #     #Ahora que el usuario esta creado con todas las caracteristicas necesarias, se procede a crear el perfil
#     #     #La idea es que el perfil se cree inmediatamente se crea el usuario. 
#     #     #Crear instancia de Profile para crear un perfil con estos datos. En este caso se crea usando los datos de user (Password y username)
#     #     #En el modelo Profile hay mas valores (biografy, phone number ...). Sin embargo, por el momento solo se tiene los valores password y username
#     #     #El usuario despues podrá entrar a su perfil para poder agregar esos valor pero para crear una cuenta solo se necesita lo minimo
#     #     profile=Profile(user=user)
#     #     #Guardar estos valores en la base de datos
#     #     profile.save()

#     #     #Direccionar el usuario al login para que pueda acceder al perfil que acaba de crear
#     #     return redirect('login')

#     # return render(request,'users/signup.html')

#     #Ahora se vuelve a hacer el sign up pero usando forms
#     if request.method=='POST':
#     #     #Usar la estructura de la documentación
#     #     #Tomar la info de la request, validar si es correcta, si lo es guardarla y redirect a login
        
#         form=SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('users:login')
#     else:
#         form = SignupForm()

#     return render(
#             request=request,            
#             template_name='users/signup.html',
#             context={'form':form}
#         )


    
#logout_view usando class-based views
#Usar la estructura de la documentación: https://docs.djangoproject.com/en/2.0/topics/auth/default/#module-django.contrib.auth.views
#Se usa loginrequred para garantizar que solo pueda salir si ya entro a un usuario
class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    """Logout view."""
    #Definir template que en este caso no hace nada
    template_name='users/logged_out.html'
    #Se debe definir el LOGOUT_REDIRECT_URL en settings que es la url donde se va cuando se termina el logout




#logout_view usando funciones
#Decorador para que solo se vean la lista de posts si hay un login registrado
#Para esto también se debe colocar en LOGIN_URL en settings y importar el modulo necesario
#Para mas información: https://docs.djangoproject.com/en/2.0/topics/auth/default/#authentication-in-web-requests
@login_required
def logout_view(request):
    """Logout view"""
    #Estructura de una logout. Mirar documentación para mas detalles: https://docs.djangoproject.com/en/2.0/topics/auth/default/#authentication-in-web-requests
    logout(request) 
    #Se retorna a la pagina donde debe ir sale de session
    return redirect('users:login')
    #Para verifica que se salió de session se intentar ver la url /post
    #La cuál se especifico que solo se puede ser si tienes un perfil iniciado


#update_profile con class-based view
class UpdateProfileView(LoginRequiredMixin,UpdateView):
    """Update profule view."""
    #Seguir la estructura de documentación: https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-editing/#django.views.generic.edit.UpdateView
    #Ubicación del template
    template_name = 'users/update_profile.html'
    #Modelo con la información del perfil
    model = Profile
    #Campos para modificar
    fields= ['website', 'biography', 'phone_number', 'picture']
    def get_object(self):
        """Return user's profile"""
        return self.request.user.profile
    
    def get_success_url(self):
        """Return to user's profile."""
        #Se crea un función para tomar el username porque la url necesita ese argumento
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})



# #update_profile con funciones
#Para usarlo se debe importar el forms ProfileForm
# #Decorador para garantizar que hay una sesión iniciada para poder actualizar el perfil
# @login_required
# def update_profile(request):
#     """Update a user's profile view."""
#     #Para hacer esto, se debe haber creado una clase forms.py he importarla 
#     #Traer el perfil en cuestión con:
#     profile=request.user.profile
#     #Se utiliza el form porque los updates puede ser muchos (repetitivos) y estos son ideleas para estos casos
#     #Seguir la estructura de la documentación: https://docs.djangoproject.com/en/2.0/topics/forms/
#     if request.method == 'POST':
#         #La idea es que para actualizar, entre en el form a validar los campos de info
#         #form será un instancia de ProfileForm y tomará los datos de la request
#         #Además de posts se pasa files porque es donde están almacenados los archivos
#         #De esta manera se pueden recibir las fotos del perfil
#         form = ProfileForm(request.POST, request.FILES)
#         #Crear validación
#         if  form.is_valid():
#             #El print es solo para revisar que los datos fueron recibidos
#             # print(form.cleaned_data)
#             #Esta es la variable que toma toda la información suministrada
#             data=form.cleaned_data
#             #Guardar las variables recibidas
#             profile.website = data['website']
#             profile.phone_number = data['phone_number']
#             profile.biography = data['biography']
#             profile.picture = data['picture']
#             profile.save()

#             #Redireccionar a update_profile para mostrar que se logro ingresar
#             #La url "detail" necesita de un argumento (user) para funcionar 
#             #Porque es el que se encarga de mostrar el perfil del usuario
#             #Así que se coloca una estrucutra adicional para que reciba argumento por default
#             #Se usa primero un reverse  para crear una url porque redirect no puede redireccionar a una url que necesite argumentos 
#             #En este caso toma 'username' como entrar a la info de la solicitud y tomar el usarname
#             url=reverse('users:detail', kwargs={'username':request.user.username})
#             return redirect(url)

#     else:
#         #Sino se ve a actualizar el perfil, no hacer nada. Solo delver la información
#         form=ProfileForm()


#     #¿Que significa esto?
#     #Información del profile del user
#     #profile=request.user.profile

#     return render(
#         request=request,
#         template_name='users/update_profile.html',
#         #Agregar contexto para no usar request.profile.user
#         context={
#             'profile': profile,
#             'user': request.user,
#             'form':form
#         }
#     )