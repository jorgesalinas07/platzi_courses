"""User forms."""

#Importar modulo para usar forms
from django import forms
from django.forms.forms import Form
#Importar base de datos con los usuarios para poder validar si ya fue creado el usuario con ese nombre 
from django.contrib.auth.models import User
#Importar los perfiles para poder crear un perfil cada que se cree un usuario
from users.models import Profile



#Crear clase con el estilo de la documentación:
#https://docs.djangoproject.com/en/2.0/topics/forms/

#El signup ya fue realizado en views de posts pero no es conveniente usar logia en una vista
#Por tal motivo se realiza la logia en un form para que view solo reciba el código
class SignupForm(forms.Form):
    """Signup form"""
    #Se usan los fields de los forms para tomar la información
    #Esto según la documentación de: https://docs.djangoproject.com/en/2.0/ref/forms/fields/
    username= forms.CharField(min_length=4, max_length=50)
    #Se agregar un widget (validaciones) para verificar password y no mostrar al usuario con .PasswordInput()
    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput())
    #Agregar los demas campos
    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)
    #Usar  widget para validar que sea un email valido con .EmailInput()
    email=forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput())

    #Crear un validator para asegurarse de que el username digitado por el usuario no este ya registrado
    #Para esto se usa la validación en el form con la documentación:
    #https://docs.djangoproject.com/en/2.0/ref/forms/validation/
    #Siguiendo la estrucutra de la documentación
    def clean_username(self):

        """Username must be unique."""
        #Tomar la información del username digitada por el usuario
        username = self.cleaned_data['username']
        #Filtrar la información de todos los usuarios a ver si hay algún username que sea igual al digitado por el usuario
        #Duelve un valor booleano
        #Se debe haber importado la base de datos de donde se esta tomando la información que en este caso es User
        username_taken = User.objects.filter(username=username).exists()
        #Si ya esta tomado, eleva un error el cual ya se toma como error por el template y muestra el mensaje
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username
        #SIEMPRE devolver el campo una vez se haga su validación siempre que se use un clean que es el ultimo método que se llama

    #Se procede a verificar si los dos passwords digitados son correctos
    #Para esto se una el form de la validación cuado hay dependecia según:
    #https://docs.djangoproject.com/en/2.0/ref/forms/validation/
    
    def clean(self):
        """Verify password confirmation match"""
        #Ahora se siguen los pasos de la documentación
        #Traer los datos
        data = super().clean()
        #Tomar los valores de password de la información
        password = data['password']
        password_confirmation = data['password_confirmation']
        #Validar si son iguales. Si no lo son elevear error que ya el .html detecta y muestra el mensaje
        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')
        #Si no hay error, retornar la información intacta
        return data


    #Crear método para guardar los datos una vez pase todos los filtros que debe
    def save(self):
        """Create user and profile"""
        #Cada que se crea un usuario se le debe crear un profile automaticamente
        #Se deben importar los perfiles
        #Tomar toda la info escrita por el user
        data=self.cleaned_data
        #No se va a guardar el password confirmation así que se elimina con pop()
        data.pop('password_confirmation')
        #Crear el usuario dandole a la clase User el comando create_user con toda la info
        #Tipo de archivo diccionario entregada por el usuario. Para que una función reciba multiples argumentos como diccionarios se usa **data
        user=User.objects.create_user(**data)
        #Ahora crear profile con instancia de la clase Profile que solo recibe user como parametro
        profile = Profile(user=user)
        #Guardar el perfil
        profile.save()

#Clase para el perfil
#No se necesita cuando se una class-based views 
# class ProfileForm(forms.Form):
#     """Profile form."""

#     #Definir los valores que se van a recibir y concurden con los de models
#     #En este caso, el campo website si es required porque así esta especificado en el middleware
#     website = forms.URLField(max_length=200, required=True)
#     biography = forms.CharField(max_length=500, required=False)
#     phone_number = forms.CharField(max_length=20, required=False)
#     picture = forms.ImageField() 