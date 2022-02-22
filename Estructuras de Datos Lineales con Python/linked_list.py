from ast import Delete
from locale import currency
from node import Node

class SinglyLinkedList:
    def __init__(self):
        #A penas se crea la linked list no hay ningun valor así que se coloca que la cabeza es nada y el tamaño es 0
        #Inicial mente el ultimo nodo (tail) no representa a ningun nodo
        self.tail = None
        #Tamaño inicialmente es 0 porque inicialmente no tiene nodos
        self.size = 0
    
    #Método para añadir nodos con el atributo data que es info del nodo que se va agregar
    def append(self, data):
        """ Se crea el nodo y si es el primero, se guarda como cabeza. Si no lo es"""
        #Tomar la info de una instancia de Node  
        node = Node(data)

        #Validar casos para guardar Nodos.
        #Caso en el que no hay un nodo
        if self.tail == None:
            #Guardar le nodo que se acaba de instancias con NODE. Como en este caso esta solo es nodo, se aplica el valor por
            #defecto en el que next es none para que no redirija a nada
            self.tail = node
        else:
            #Saber donde estamos actualmente. Se crea la varialbe current que ubica la cabeza
            current = self.tail
            #Modificar donde se encuentra current. Cada que el siguiente valor no se None (tenga alguna referencia en next)
            #Mover current a la siguiente posición para ir recorriendo los nodes. Se sale cuando llega al ultimo, es decir, cuando no hay mas next (=None)
            while current.next != None:
                current = current.next
            #Cuando lleguemos al ultimo, se agrega el nuevo nodo. El cuál, tiene next = none así que se hará le mismo proceso hasta ñegar a este cuando se agregue otro nodo
            current.next = node

        #Aumentar el tamaño del nodo por el nodo que se acaba de crear
        self.size += 1

    #Definir método para calcular tamaño del nodo
    def size(self):
        return str(self.size)
    
    #Iterador para tomar y recorrer sus valores
    def iter(self):
        """ Función que recorre toda la lista y devuelve el valor de cada posición que toma """
        current = self.tail
        while current!= None:
            #Dato del valor actual
            val = current.data
            #Pasar al siempre nodo
            current = current.next
            yield val
    
    def delete(self, data):
        if self.size == 0:
            return False
        else:
            #Referencia a final y principio porque van cambiando a lo largo del proceso
            current = self.tail
            previous = self.tail
            #El while se ejecuta hasta que llega al final que es cuando current (que despues se refine como current.next, es decir,
            # la referencia al siguiente nodo) es = none
            while current != None:
                #El if se encarga de buscar el valor en cada iteración y para la iteración cuando encuentra y se ubica en el valor
                if current.data  == data:
                    if current == self.tail:
                        #Valor del nodo siguiente
                        self.tail = current.next
                    else:
                        #Para el caso en el no nos encontramos en la cabeza sino en un valor dentro de la lista, se hace que previous al valor actual
                        #sea el next del valor actual (saltarse un elemento). El nodo guardado en preview cambia su referencia  el nodo donde termina el salto
                        previous.next = current.next
                        # Se disminuye el tamaño de la lista por el elemento saltado
                        self.size -= 1
                        #Se devuelve el valor eliminado
                        return current.data
                #Estas dos variables se encargan de que se vaya recorriendo la lista. Cuando termina un iteración, previous toma el valor actual en la lista
                #Y current toma el siguiente valor de la lista
                #Sin embargo, toma un significado diferente cuando se encuentra el valor y se realiza el salto del elemento (proceso en el else). 
                # En este caso, ya se cambio la referencia en el nodo en previous por lo que una vez se siga a previous = current, el nodo ya no referenciará al nodo se que desea eliminar
                previous = current
                current = current.next
    


    def search(self,data):
        for node in self.iter():
            if data == node:
                print(f"Data {data} found!")
            else:
                print(f"Data {data} was not found!")
    
    #Limpiar lista
    def clear(self):
        #tail y head no tienen nada así que se limpia todo
        self.tail = None
        self.head = None
        self.size = 0
    

# >>> from linked_list import SinglyLinkedList
# >>> words = SinglyLinkedList()
# >>> words.append('egg')
# >>> words.append('ham')
# >>> words.append('spam')
# >>> current = words.tail
# >>> while current:
# ...     print(current.data)
# ...     current = current.next
# ... 
# egg
# ham
# spam
# >>> for word in words.iter().
#   File "<stdin>", line 1
#     for word in words.iter().
#                             ^
# SyntaxError: invalid syntax
# >>> for word in words.iter():
# ...     print(word)
# ... 
# egg
# ham
# spam
# >>> words.search(spam)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'spam' is not defined
# >>> words.search("spam")
# Data spam found!
# >>> words.search("juice")
# >>> words.clear()
# >>> while current:
# ...     print(current.data)
# ...     current = current.next