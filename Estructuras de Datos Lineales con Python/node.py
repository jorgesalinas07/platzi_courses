class Node():
    # Se toma el valor de data que tiene el valor del nodo y next que es la refencia al siguiente nodo. Por defecto no referencia a nada
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

# >>> node1 = None
# >>> node2=Node("A",None)
# >>> node3=Node("B",node2)
# >>> node2
# <node.Node object at 0x7fb7f3a49cd0>
# >>> node2.data
# 'A'
# >>> node2.next
# >>> node3.next
# <node.Node object at 0x7fb7f3a49cd0>
# >>> node3.next.data
# 'A'