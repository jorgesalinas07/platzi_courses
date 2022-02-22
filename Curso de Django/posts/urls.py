"""Post URLs."""

#Django
#Registra urls con path
from django.urls import path

#Views
#Registrar vistas
from posts import views

urlpatterns=[
    #url para mirar los posts
    #Las views de class-based views siempre llevan la estrutura:
    #views.nombredelaclase.as_view
    path(
        route='',
        view=views.PostsFeedView.as_view(), 
        name='feed'
    ),
    #Crear url para crear un post con método función
    # path(route='posts/new/', 
    #     view=views.create_post, 
    #     name='create'
    #     ),
    #Crear url para crear un post con class-based view
    path(
        route='posts/new/',
        view=views.CreatePostView.as_view(),
        name='create',
    ),
    #Crear url para el detalle de un post
    #La ruta tendrá el pk de la publicación
    #La vista será una class-based view de nombre PostDetailView
    path(route= 'post/<int:pk>',
    view=views.PostDetailView.as_view(),
    name='detail',
    )
]