import sys
#Modulo para importar Readers
import csv

import os

#Los archivos con punto inicial, para declarar archivos, hacen referencia a un archivo oculto.
CLIENT_TABLE = '.clients.csv'
#Lista de llaves que usa csv para construir diccionarios
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []

def _initialize_clients_from_storage():
    """ Look in the storage of clients """
    with open(CLIENT_TABLE, mode='r') as f:
        #DictReader sirve para poder leer archivos csv como diccionarios
        #Se le debe pasar el archivo que va a leer y una lista de llaves (fieldnames) para construir diccionarios
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)
        #Agregar el elemento de cada fila del reader a clients
        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    """Funcion guarda la información en bdd. Para esto, guarda en una tabla temporal que se va borrando 
    y creado cada que se agrega un nuevo cliente"""
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    #Abir archivo en modo writer para guaradar elemento
    with open(tmp_table_name, mode = 'w') as f:
        #DictWriter usa los mismos comandos de DictReader
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        #Usar todas las filas de clients con writerows. Si se quisiera usar solo una fila sería writerow 
        writer.writerows(clients)

        #Borrar tabla original
        os.remove(CLIENT_TABLE)
        #Renombrar tabla actual
        os.rename(tmp_table_name, CLIENT_TABLE)

def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already in client\'s list')


def list_clients():
    print('uid |  name  | company  | email  | position ')
    print('*' * 50)

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx, 
            name=client['name'], 
            company=client['company'], 
            email=client['email'], 
            position=client['position']))


def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Client not in client\'s list')


def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx] 
            break


def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _get_client_field(field_name, message='What is the client {}?'):
    field = None

    while not field:
        field = input(message.format(field_name))

    return field


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?:')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


if __name__ == '__main__':
    _initialize_clients_from_storage()

    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = _get_client_from_user()

        create_client(client)
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()

        update_client(client_id, updated_client)
    elif command == 'D':
        client_id = int(_get_client_field('id'))

        delete_client(client_id)
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)
        
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')
    
    _save_clients_to_storage()