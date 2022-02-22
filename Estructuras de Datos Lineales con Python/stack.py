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


# >>> from stack import Stack
# >>> food = Stack()
# >>> food.push("egg")
# >>> food.push("ham")
# >>> food.push("spam")
# >>> food.pop()
# 'spam'
# >>> food.peek()
# 'ham'
# >>> food.clear()
# >>> food.peek()
# 'The stack is empty'