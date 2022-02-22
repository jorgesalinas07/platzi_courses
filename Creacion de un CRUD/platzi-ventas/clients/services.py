import csv
import os

from clients.models import Client

#GUardar la lógica de negocio (CRUD)
class ClientService:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self, client):
        #Abrir tabla de nombre definido con modo append. ESto porque cada que venga un nuevo cliente se va a añadir
        #row con la nueva info0
        with open(self.table_name, mode='a') as f:
            #Se usa DictWriter porque se va a agregar rows. Tomar los fieldnames del archivo models
            writer = csv.DictWriter(f, fieldnames= Client.schema())
            #Agregar el nuevo cliente recibido con un row nueva. Para esto se pasa el cliente recibido como parametro a diccionario
            # Esto para que se pueda recibir
            writer.writerow(client.to_dict())

    def list_clients(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())
            return list(reader)

    def update_client(self, updated_client):
        #Tomar lista de clientes
        clients = self.list_clients()
        #Buscar el cliente 
        updated_clients = []
        for client in clients:
            #
            if client['uid'] == updated_client.uid:
                #Usar to_dic() cuando se usa CSV
                updated_clients.append(updated_client.to_dict())
            else:
                updated_clients.append(client)

        self._save_to_disk(updated_clients)

    def delete_client(self, client_uid):
        clients = self.list_clients()
        updated_clients = [client for client in clients if client['uid'] != client_uid]

        self._save_to_disk(updated_clients)

    def _save_to_disk(self, clients):
        """ SAVE WITH TEMPORAL TABLE """
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name, mode='w') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerows(clients)

        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)
