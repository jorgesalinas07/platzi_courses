# >>> from node import Node
# >>> head = None
# >>> for count in range(1,6):
# ...     head = Node(count,head)
# ... 
# >>> while head != None:
# ...     print(head.data)
# ...     head = head.next
# ... 
# 5
# 4
# 3
# 2
# 1
# >>> probe = head
# >>> while probe != None:
# ...     print(probe.data)
# ...     probe = probe.next
# ... 
# >>> probe = head
# >>> target_item = 2
# >>> while probe != None and target_item != probe.data:
# ...     probe = probe.next
# ... 
# >>> if probe != None:
# ...     print(f"Target item {target_item} has been found")
# ... else:
# ...     print(f"Target item {target_item} is not in the linked list")
# ... 
# Target item 2 is not in the linked list
# >>> probe = head
# >>> target_item = 3
# >>> new_item = "Z"
# >>> while probe != None and target_item != probe.data:
# ...     probe = probe.next
# ... 
# >>> if probe != None:
# ...     probe.data = new_item
# ...     print(f"{new_item} replaced the old value in the node number {target_item}")
# ... else:
# ...     print(f"The target item {target_item} is not in the linked list")
# ... 
# The target item 3 is not in the linked list
# >>> #head = None
# >>> head = Node("F", head)
# >>> #Nuevo nodo al final de la lista
# >>> new_node = Node("K")
# >>> #Colocar nodo al principio o al final. Si no hay nodo, lo coloca como primer nodo. Si hay nodos, lo coloca como ultimo nodo
# >>> if head is None:
# ...     head = new_node
# ... else:
# ...     probe = head
# ...     while probe.next != None:
# ...             probe=probe.next
# ...     probe.next = new_node
# ... 
# >>> removed_item = head.data
# >>> head = head.next
# >>> print(removed_item)
# F
# >>> #Remover valor al final
# >>> removed_item = head.data
# >>> if head.next is None:
# ...     head = None
# ... else:
# ...     #El caso anterior es para el caso en el que solo hay un valor en la lista. Para el siguiente caso es cuando hay mas valores      
# ...     #Se recorre toda la lista hasta ubicarse a dos casillas antes de none (es decir, una antes del calor a borrar
# ...     while probe.next != None:
# ...             probe = probe.next
# ...     #Se guarda el valor que se va a remover
# ...     removed_item = probe.next.data
# ...     #Borrar el dato
# ...     probe.next = None
# ... 
# >>> print(removed_item)
# K
# >>> #Añadir elemento en una posición determinada
# >>> #Pedir elemento al usuario
# >>> new_item = input("Enter new item: ")
# Enter new item: 10
# >>> index = int(input("Enter the position to insert the new item: "))
# Enter the position to insert the new item: 3
# >>> if head is None or index<0:
# ...     #En el caso en el que no haya nodos, se crea un primer nodo con valor de py que referencia a none porque ese es el valor inicial de head
# ...     head = Node("Py", head)
# ... else:
# ...     #Para el caso en el que no este vacio: Se busca la posición que definió el usuario y aí se ubica el nuevo valor
# ...     probe = head
# ...     #Se recorre solo cuando no se haya llegado a 1 en el index y que no se haya llegado al final
# ...     while index>1 and probe.next != None:
# ...             probe = probe.next
# ...             #Disminuir el index para que salga cuando llegue a 1, es decir la posición del nuevo elemento
# ...             index -= 1
# ...     #Al llegar a la ubicación, se remplaza el valor y se referencia la siguiente nodo
# ...     probe.next = Node(new_item, probe.next)
# ... 
# >>> #Eliminar nodo de una posición
# >>> index = 3
# >>> if index <= 0 or head.next is None:
# ...     #Para el caso en el que solo hay un elemento
# ...     removed_item = head.data
# ...     #Tomar la cabeza como el siguiente valor (none)
# ...     print(removed_item)
# ... else:
# ...     #Para el caso en el que hay mas de un elemento en la lista: Recorrer toda la lista hasta la posición buscada
# ...     #Para eso hay que ir disminuyendo los index hasta llegar al valor
# ...     probe = head
# ...     while = index > 1 and probe.next.next != None:
#   File "<stdin>", line 10
#     while = index > 1 and probe.next.next != None:
#           ^
# SyntaxError: invalid syntax
# >>> #Eliminar nodo de una posición
# >>> index = 3
# >>> if index <= 0 or head.next is None:
# ...     #Para el caso en el que solo hay un elemento
# ...     removed_item = head.data
# ...     #Tomar la cabeza como el siguiente valor (none)
# ...     print(removed_item)
# ... else:
# ...     #Para el caso en el que hay mas de un elemento en la lista: Recorrer toda la lista hasta la posición buscada
# ...     #Para eso hay que ir disminuyendo los index hasta llegar al valor
# ...     probe = head
# ...     while index >1 and probe.next.next != None
#   File "<stdin>", line 10
#     while index >1 and probe.next.next != None
#                                              ^
# SyntaxError: invalid syntax
# >>> if index <= 0 or head.next is None:
# ... ...     #Para el caso en el que solo hay un elemento
#   File "<stdin>", line 2
#     ...     #Para el caso en el que solo hay un elemento
#     ^
# IndentationError: expected an indented block
# >>> ...     removed_item = head.data
#   File "<stdin>", line 1
#     ...     removed_item = head.data
#             ^
# SyntaxError: invalid syntax
# >>> ...     #Tomar la cabeza como el siguiente valor (none)
# Ellipsis
# >>> ...     print(removed_item)
#   File "<stdin>", line 1
#     ...     print(removed_item)
#             ^
# SyntaxError: invalid syntax
# >>> ... else:
#   File "<stdin>", line 1
#     ... else:
#         ^
# SyntaxError: invalid syntax
# >>> ...     #Para el caso en el que hay mas de un elemento en la lista: Recorrer toda la lista hasta la posición buscada
# Ellipsis
# >>> ...     #Para eso hay que ir disminuyendo los index hasta llegar al valor
# Ellipsis
# >>> ...     probe = head
#   File "<stdin>", line 1
#     ...     probe = head
#             ^
# SyntaxError: invalid syntax
# >>> ...     while index >1 and probe.next.next != None
#   File "<stdin>", line 1
#     ...     while index >1 and probe.next.next != None
#             ^
# SyntaxError: invalid syntax
# >>> #Eliminar nodo de una posición
# >>> index = 3
# >>> #Para el caso en el que solo hay un elemento
# >>> if index <= 0 or head.next is None:
# ...     removed_item = head.data
# ...     head = head.next
# ...     print(removed_item)
# ... else:
# ...     #En el caso en el que hay mas de un nodo: Registrar toda la lista hasta llegar al index correcto y remplazar el valor
# ...     probe = head
# ...     while index > 1 and probe.next.next != None:
# ...             probe = probe.next
# ...             index -= 1
# ...             #Se recorre toda la lista hasta llegar a na posición antes de la que deseada
# ...     removed_item = probe.next.data
# ...     #Guardar item borrado
# ...     prone.next = probe.next.next
# ...     probe.next = probe.next.next
# ...     #Hacer que el ultimo nodo sea el de dos puestos adelante (None)
# ...     print(removed_item)
# ... 
# Py
