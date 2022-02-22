import random
from functools import reduce
#Clase para crear un arreglo con todas las caracteristicas
class Arreglo():

    #Sus variables son la capacidad o tamaño y el valor con le que se va a rellenar (none por defecto)
    def  __init__(self, capacity, fill_value=None):
        #Guadar los valores ingresados en el array en una lista
        self.items = list()
        for i  in range(capacity):
            self.items.append(fill_value)

    #Método para conocer el tamaño del array. Hacerlo como variable privada
    def __len__(self):
        return len(self.items)

    #Definir sus elementos como strings
    def __str__(self) -> str:
        return str(self.items)

    #Definir Iterador. Privado
    def __iter__(self):
        return iter(self.items)

    #Obtener elemento del array
    def __getitem__(self, index):
        #Tomar elemento en el indice proporcionado
        return self.items[index]

    #Colocar un item en el array con el index y new item solicitado
    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    def __replaceitems__(self):
        count = len(self.items)
        for i in range(count):
            self.items[i] = (random.randint(1,100))
        return self.items

    def __sumarray__(self):
        return reduce(lambda a, b: a+b, self.items)

    def __filleditems__(self):
        count = 0
        for i in range(self.items.__len__()):
            if i != None:
                count += 1
        return count
# >>> from arreglo import Arreglo
# >>> menu = Arreglo(5)
# >>> len(menu)
# 5
# >>> print(menu)
# [None, None, None, None, None]
# >>> for i in range(len(menu)):
# ...     menu[i] = i+1
# ... 
# >>> print(menu)
# >>> menu.__len__()
# 5
# >>> menu.__str__()
# '[1, 2, 3, 4, 5]'
# >>> menu.__iter__()
# <list_iterator object at 0x7fbd3c818cd0>
# >>> menu.__getitem__(2)
# 3
# >>> menu.__setitem__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: __setitem__() missing 2 required positional arguments: 'index' and 'new_item'
# >>> menu.__setitem__(2, 100)
# >>> menu.__getitem__(2)
