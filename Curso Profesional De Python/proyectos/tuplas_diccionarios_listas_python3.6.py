from typing import Tuple, Dict, List

#Crear una lista de diccionarios cuyas llaves sean strings y los valores sean tupla con dos valores enteros
coordinatestype=list[dict[str,tuple[int,int]]]

#Usar alias para usar lo anterior y crear la lista
coodinates:coordinatestype=[
    {
        'coord1':(1,2),
        'coord2':(3,5)
    },
    {
        'coord1':(0,1),
        'coord2':(2,5)
    },
]