#Importar los modulos para la declaración de listas y diccionarios
from typing import Dict, List

#Crear variable declarando que sera una lista con valores de tipo entero
positives: list[int]=[1,2,3,4,5]

#Crear diccionario declarando que será un diccionario
#Con llaves de string y valores de enteros
users: Dict[str, int]={
    "argentina":1,
    "mexico":34,
    "colombia":45,
}

#Crear una lista de diccionarios que tendrán llaves strings y valores strings

countries: List[Dict[str, str]] = [
{
    'name':'Argentina',
    'people':'450000',
},
{
    'name':'méxico',
    'people':'900000',
}
]