"""Post URLs."""

#Django
#Registra urls con path
from django.urls import path
#Importar para una vista basada en clase
from users import views


#Views
#Registrar vistas
from users import views

urlpatterns=[
    #Crear url para el perfil de usuario
    #La ruta sera el nombre del usuario
    #Crear vista basada en clase. Se debe haber importado el modulo correcto
    #Para mas info mirar docuementación
    path(
        route='profile/<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    #Crear url para el login del usuario
    path(
        route='login/', 
        view=views.LoginView.as_view(), 
        name='login'
    ),
    #Crear url para el log out del usuario
    #Crear url con funciones 
    # path(
    #     route='logout/', 
    #     view=views.logout_view, 
    #     name="logout"
    # ),
    #Crear url de log_out con class-based view
    path(
        route = 'logout/',
        view = views.LogoutView.as_view(),
        name='logout'
    ),
    #Crear url para hace singup de algún usuario
    #Se quiere que en el momento que se cree el usuario, se cree un perfil
    #url con funciones
    # path(
    #     route='signup/', 
    #     view=views.signup, 
    #     name='signup'
    # ),
    #url con clases
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='me/profile/', 
        view=views.UpdateProfileView.as_view(), 
        name='update_profile'),
]
