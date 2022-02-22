


class TwoWayNode(object):
    def __init__(self, data, previous = None, next = None):
        self.data = data
        self.previous = previous
        self.next = next

class Queue:
    def __init__(self):
        #Primer nodo
        self.head = None
        #Ultimo nodo
        self.tail = None
        #Conteo de nodos
        self.count = 0
    
    def enqueue(self, data):
        """ Add value to the queue"""
        new_node = TwoWayNode(data, None, None)
        #Caso en el que no hay datos en el archivo
        if self.head is None:
            #La cabeza y la cola son el nuevo nodo añadido
            self.head = new_node
            self.tail = self.head
        else:
            #Si hay mas nodos
            #El referencia previa del nodo nuevo va a ser el ultimo nodo acutal (tail)
            new_node.previous = self.tail
            #La referencia next del ultimo nodo actual va a ser el nuevo nodo creado
            self.tail.next = new_node
            #Por ultimo el ultimo nodo actual va a ser de ahora en adelante el nodo nuevo
            self.tail = new_node
        
        self.count += 1
    
    def dequeue(self):
        """Remove elements"""
        current = self.head
        #Si solo hay un nodo
        if self.count == 1:
            self.count -=1
            self.head = None
            self.tail = None
        elif self.count >1:
            #CUando hay mas de un nodo:
            #La cabeza cambia a ser el siguiente valor porque el primero se va a borrar
            self.head = self.head.next
            #La nueva cabeza no puede tener ningún previo
            self.head.previous = None
            self.count -= 1
        
        return current.data
