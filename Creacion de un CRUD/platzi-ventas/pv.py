# import click
# #importar comandos (todos) que se acaban de crear
# from clients import commands as clients_commands

# #Contexta da un objecto contexto que se inicia como diccionario
# @click.group()
# @click.pass_context
# def cli(ctx):
#     ctx.obj = {}

# #Registrar comandos
# cli.add_command(clients_commands.all)

import click

from clients import commands as clients_commands

#Definir el nombre de la tabla donde estarán los clientes
CLIENTS_TABLE = '.clients.csv'


@click.group()
@click.pass_context
def cli(ctx):
    """An application to manage clients, inventory, sales and produce reports."""
    ctx.obj = {}
    #Añadir la tabla que se usa para guardar los datos al contexto
    ctx.obj['clients_table'] = CLIENTS_TABLE


cli.add_command(clients_commands.all)