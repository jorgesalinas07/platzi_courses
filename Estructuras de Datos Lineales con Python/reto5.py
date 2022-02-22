#Crear stack con nuevos métodos:
# 1. Buscar un elemento en particular. 2. Recorrerlo (iterador). 3. Vaciar stack de una manera diferente
# 4. Crear stack basada en array (basarse en el indice del array)

from array import array
from itertools import count
from multiprocessing.dummy import Array
from textwrap import fill
from typing import Counter
from node import Node
from arreglo import Arreglo
class ArrayStack(Arreglo):
    def __init__(self, capacity, fill_value = None):
        #Cuando esta vacion no hay top, el tamaño empieza en 0 pero puede ir creciendo
        self.top = None
        self.size = 0
        self.capacity = capacity
        Arreglo.__init__(self, capacity=capacity, fill_value=fill_value)
    

    def push(self, data):
        """Funtion to add values"""
        if self.size== self.capacity:
            print("The stack is full")
        else:
            if self.top != None:
                #El top top actual, se mueve al siguiente nodo del que se acaba de crear. El nuevo top es el nodo que se acaba de crear
                for i in range(self.size,-1,-1):
                    if i == self.capacity-1:
                        continue
                    else:
                        self.items[i+1]  = self.items[i]
                self.top = data
                self.items[0] = data
            else:
                self.top = data
                self.items[0] = data
            self.size += 1

    def pop(self):
        """Remove the top value in the stack"""
        #Si hay elementos
        if self.top != None:
            #Se toma el valor del top y se disminuye el tamaño
            data = self.top
            for i in range(self.size):
                if i == self.capacity-1:
                    break
                else:
                    self.items[i]  = self.items[i+1]
            self.items[self.size-1]=None
            self.size -= 1
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
        """Remove all elements of the stack"""
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
        probe = self.items
        count = 0
        while count<=self.size:
            #Dato del valor actual
            val = probe[count]
            count += 1
            yield val

    def clear2(self):
        """Remove all elements of the stack"""
        self.top = None
        self.size = 0

if __name__ == "__main__":
    l = ArrayStack(5)
    l.push("a")
    l.push("b")
    l.push("c")
    l.push("l")
    l.push("r")
    print(l)
    # print(l.size)

    # print(l.pop())
    # print(l.size)
    # print(l)
    # for i in l.__iter__():
    #     print(i)
    print(l.clear())