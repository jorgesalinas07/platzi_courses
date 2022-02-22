from arreglo import Arreglo
from node import Node
from linked_list import SinglyLinkedList

size = 5
lista = Arreglo(size).__replaceitems__()
print(lista)
nodes = SinglyLinkedList()
for i in range(size):
    nodes.append(data=lista[i]) 

current = nodes.tail
while current:
    print(current.data)
    current = current.next