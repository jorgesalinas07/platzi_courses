#Crear stack con nuevos métodos:
# 1. Buscar un elemento en particular. 2. Recorrerlo (iterador). 3. Vaciar stack de una manera diferente
# 4. Crear stack basada en array (basarse en el indice del array)

from node import Node

class Stack:
    def __init__(self):
        #Cuando esta vacion no hay top, el tamaño empieza en 0 pero puede ir creciendo
        self.top = None
        self.size = 0
    
    def push(self, data):
        """Funtion to add values"""
        #Los datos vienen de los nodos
        node = Node(data)
        #Validar caso en el que hay elementos o no hay elementos dentro del stack
        if self.top != None:
            #El top top actual, se mueve al siguiente nodo del que se acaba de crear. El nuevo top es el nodo que se acaba de crear
            node.next =  self.top
            self.top = node
        else:
            self.top = node
        
        #self.size += 1

    def pop(self):
        """Remove the top value in the stack"""
        #Si hay elementos
        if self.top != None:
            #Se toma el valor del top y se disminuye el tamaño
            data = self.top.data
            self.size -= 1

            #En el caso en el que hay mas de un elemento (siguiente valor al top es != none), se reposicionan
            if self.top.next != None:
                #El nuevo top es el siguiente número
                self.top = self.top.next
            else:
                #Si queda 
                self.top = None
            #Mostrar elemento removido
            return data
        else:
            return "The stack is empty"
        
    def peek(self):
        """ Show the last element from the stack"""
        if self.top != None:
            return self.top.data
        else:
            return "The stack is empty"

    def clear(self):
        """REmove all elements of the stack"""
        while self.top != None:
            self.pop()

    def search(self, data):
        probe = self.top
        if probe.next == None:
            if probe.data == data:
                print(f"El elemento {data} se encuentra en el stack")
            else:
                print(f"El elemento {data} no se encuentra en el stack")
        else:
            while probe != None:
                if probe.data == data:
                    print(f"El elemento {data} se cuentra en el stack")
                    break
                if probe.next == None:
                    print(f"El elemento {data} no se encuentra en el stack")
                probe = probe.next
        
    def iter(self):
        """ Función que recorre toda la lista y devuelve el valor de cada posición que toma """
        probe = self.top
        while probe!= None:
            #Dato del valor actual
            val = probe.data
            #Pasar al siempre nodo
            probe = probe.next
            yield val

    def clear2(self):
        """Remove all elements of the stack"""
        self.top = None
        self.size = 0