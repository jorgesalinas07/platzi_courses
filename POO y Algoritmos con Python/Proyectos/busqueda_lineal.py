import random

def busqueda_lineal(lista, objetivo):
    match= False
    #Buscar algún match
    for elemento in lista:
        if elemento==objetivo:
            match=True
            break
    
    return match

if __name__=="__main__":
    #Pedir info al usuario
    tamano_De_lista=int(input("De que tamaño será la lista?"))
    objetivo=int(input("Que numero quieres encontrar?"))
    #Crear lista aleatoria del tamaño que dice el usuario
    lista=[random.randint(0,100) for i in range (tamano_De_lista)]
    #Ejecutar función y esperar recibir un False o True
    encontrado=busqueda_lineal(lista,objetivo)
    print(lista)
    #Mostrar la conclusión si se encontró o no.
    #Se usa una sintaxis para usar if en el print
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')