"""Este form se encarga de verificar que los datos ingresados por el usuario están de acuerdo a los solicitados"""

#Django
from django import forms

#Models
from posts.models import Post

#
#Seguir la estructura de un form de la documentación:  https://docs.djangoproject.com/en/2.0/topics/forms/
#Normalmente el argumento sería forms.form pero como se usarán los modelform se usa forms.ModelForm
class PostForm(forms.ModelForm):
    """Post model form."""
    #Ahora continuar con la estrctura de la documentación de modelform
    #https://docs.djangoproject.com/en/2.0/topics/forms/modelforms/

    class Meta:
        """Form settings"""
        #Importar los campos del modelo de post
        #Primero va la clase que tiene el modelo
        model=Post
        #Después los campos que se van a tomar
        fields=('user', 'profile','title','photo')
