# >>> from node import Node
# >>> index = 1
# >>> new_item = "ham"
# >>> head = Node(None, None)
# >>> head.next = head
# >>> #Se esta refenciando asi mismo para hacer el link circular
# >>> probe = head
# >>> while index>0 and probe.next != head:
# ...     #while para cuando indice no se ha terminado y para cuando el siguiente nodo no ha llegado al primero (1ra vuelta)
# ...             probe = probe.next
# ...             index -= 1
# ... 
# >>> probe.next= Node(new_item, probe.next)
# >>> print(probe.next.data)
# ham
from platform import node
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

# >>> head = Node(None, None)
# >>> head.next = head
# >>> #Se esta refenciando asi mismo para hacer el link circular
probe = nodes.tail
while size>0 and probe.next != None:
    #while para cuando indice no se ha terminado y para cuando el siguiente nodo no ha llegado al primero (1ra vuelta)
            probe = probe.next
            size -= 1

probe.next= Node("new_item", probe.next)
print(probe.next.data)