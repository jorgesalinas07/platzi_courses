# import click

# #Decorador group convierte a la función clients enotro decorador
# @click.group()
# #Definir el grupo a donde pertenecen las otras funciones
# def clients():
#     """ Manages the clientes lifecycles """
#     pass


# #Para convertir todos a comando se usa el decorador command. Se le pasa el contexto tambien
# @click.command()
# @click.pass_context
# def create(ctx, name, company, email, position):
#     """ Creates a new client """
#     pass


# @click.command()
# @click.pass_context
# #Funcion recibe contexto(diccionario creado en pv.py)
# def list(ctx):
#     """ List all clients """
#     pass


# @click.command()
# @click.pass_context
# def update(ctx, client_uid):
#     """ Updates a client """
#     pass


# @click.command()
# @click.pass_context
# def delete(ctx, client_uid):
#     """ Deletes a client """
#     pass

# #Alias para declarar todas las funciones
# all = clients

import click

from clients.services import ClientService
from clients.models import Client


@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass

#Se definen opciones porque se necesita los valores del usuario para crearlo
@clients.command()
#Definir las opciones para el usuario para que pueda escoger que va a hacer con el programa
@click.option(
                #Definir el short y e nombre de la opción
                '-n', '--name',
              type=str,
              #Definir True para que si el usuario no da la opción, pedirselo
              prompt=True,
              #Ayuda si el usuario usa el comando help
              help='The client\'s name')
@click.option('-c', '--company',
              type=str,
              prompt=True,
              help='The client\'s company')
@click.option('-e', '--email',
              type=str,
              prompt=True,
              help='The client\'s email')
@click.option('-p', '--position',
              type=str,
              prompt=True,
              help='The client\'s position')
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new client"""
    #Iniciar un cliente con toda su info (id generato automatico)
    client = Client(name, company, email, position)
    #Tomar una acción o service del usuario
    client_service = ClientService(ctx.obj['clients_table'])

    #Usar el serivicio create con la info entregada
    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    #Crear instancia de clientservice usando clients_table como contexto
    client_service = ClientService(ctx.obj['clients_table'])
    #Tomar la lista de clientes tomada del dicionario y mostrarla
    clients = client_service.list_clients()
    #.echo es mejor practica para imprimir
    click.echo('ID  |  Name  |  Company  |  Email  |  Position')
    click.echo('-' * 100)
    for client in clients:
        click.echo('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=client['uid'],
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))


@clients.command()
@click.argument('client_uid',
                type=str)
@click.pass_context
def update(ctx, client_uid):
    """Updates a single client"""
    client_service = ClientService(ctx.obj['clients_table'])

    client = [client for client in client_service.list_clients() if client['uid'] == client_uid]
    
    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)

        click.echo('Client updated')
    else:
        click.echo('Client not found')


def _update_client_flow(client):
    click.echo('Leave empty if you don\'t want to modify a value')

    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str, default=client.company)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.position = click.prompt('New position', type=str, default=client.position)

    return client


@clients.command()
@click.argument('client_uid',
                type=str)
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    client_service = ClientService(ctx.obj['clients_table'])

    if click.confirm('Are you sure you want to delete the client with uid: {}'.format(client_uid)):
        client_service.delete_client(client_uid)


all = clients