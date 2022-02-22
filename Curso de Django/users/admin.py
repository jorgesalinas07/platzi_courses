"""User admin classes."""

#Djando
from django.contrib import admin
from django.db.models.base import Model

#Modulo necesario para externder el usuario
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#Models
from users.models import Profile
from django.contrib.auth.models import User
from posts.models import Post

#Registrar el modelo para que aparezca en la pagina web
#admin.site.register(Profile)

#Otra forma de registrar un usuario (la manera recomendada):
#Decorador para registrar
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""
    #Modificar los campos a mirar en la lista de perfiles
    list_display=('pk', 'user','phone_number', 'website', 'picture')
    #Hacer que se pueda entrar al usuario dandole click a cualquier campo de la lista.
    #Ej: darle click a phone_number y que se abra toda la info del usuario
    list_display_links=('pk','user')
    #Hacer que se pueda editar un valor de la lista sin necesidad de entrar a la info del usuario
    #Nota: Si es editable no puede estar en "display_links" (punto anterior)
    list_editable=('phone_number', 'website', 'picture')
    #Agregar barra de busqueda para poder por atributos en los perfiles
    search_fields=('user__email',
                   'user__first_name',
                   'user__last_name',
                   'phone_number')

    #Crear lista para filtrar los usuarios por fecha
    #Crea una tabla a la derecha de la pagina donde se ven los filtros
    #Para este caso los filtros son:
    #Por cuando fueron creados y modificados, si el user esta activo o no y si es staff o no
    #El orden en el que se coloque aquí es el orden en el que se muestra en la pagina
    list_filter=('created',
                 'modified',
                 'user__is_active',
                 'user__is_staff',
                 )
    
    #Comando de admin site para 
    #Son tuplas. La primera es el titulo y la segunda es un diccionario
    #Usando la llave "fields" se escoge lo que mostrara en los valores que deben ser tuplas
    # fieldsets=(
    #     ('Profile',{
    #         'fields':('user','picture'),
    #     }),
    # )
    
    #Si queremos que la tupla este una al lado de la otra
    fieldsets=(
        ('Profile',{
            'fields':(
                ('user','picture'),
                ('phone_number','website'),
            ),
        }),
        # ('Extra info',{
        # 'fields':(
        #     ('website','phone_number'),
        #     ('biography')
        # )
        # }),
        ('Metadata',{
            'fields':(('created','modified'),),
        })
    )

    #Crear variable que tendra los valores que no se podrán editar en el fildsets
    #Como es un tupla no debería poder editarse pero hay algunas varibles que se pueden editar por defecto
    #Si no hacemos estos, eleva la exception 'created' cannot be specified for Profile model form as it is a non-editable field
    readonly_fields=('created','modified',)


#Crear clase con stackedInline para extender el user model a el profile
#De esta manera se puede crear el perfil de usurio en el mismo momento en el que este se crea
#Se debe importar el modulo necesario.
#Seguir documentación: https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model
class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""
    #Variables requeridas de documentación
    model=Profile
    can_delete=False
    verbose_name_plural='profiles'

#Crear clase para el mismo objetivo (extender el usuario)
class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""
    #Debe ser tupla así que debe llevar la coma, sino da excepción
    inlines=(ProfileInline,)
    #Esto se hace para demostrar que solo se esta sobre escribiendo la base de datos
    list_display=(
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )
#Para que estas clases funcionen se debe desregistrar el profileinline
#Y despues registrar UserAdmin

admin.site.unregister(User)
admin.site.register(User,UserAdmin)

#Se registra otro admin para poder ver los Posts desde admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('user', 'title', 'photo')

