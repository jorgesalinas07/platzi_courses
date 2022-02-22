import random
#Se define la funcion con sus paremetros
def busqueda_binaria(lista, comienzo, final, objetivo,contador=0):
    #Observar cuales son los valores que va tomando como max y min
    #Como se viene de un len() se debe colocar final con -1
    contador+=1
    print(f"Buscando {objetivo} entre {lista[comienzo]} y {lista[final-1]}")
    
    #Si comienzo es mayor a final significa que no recorrio toda la lista y no se encontró el valor
    #Si no entra es porque aún podemos continuar
    if comienzo>final:
        return (False,contador)
    #Se define el medio de la lista. El // dice que solo nos importa la parte entera
    medio=(comienzo+final)//2
    #Si se encontró el valor, entonces salir con true
    #Si el medio es menor que el objetivo, el nuevo comiezo es el medio+1 para acortar la lista
    #Si el medio es mayor al objetivo, el nuevo final es medio-1 para acortar la lista
    if lista[medio]==objetivo:
        return (True,contador)
    elif lista[medio]<objetivo:
        return busqueda_binaria(lista,medio+1,final,objetivo,contador=contador)
    else:
        return busqueda_binaria(lista,comienzo,(medio-1),objetivo, contador=contador)
    #Se hace el número de veces que sea necesario para retornar un valor True o False.
    
if __name__=="__main__":
    #Pedir info al usuario
    tamano_De_lista=int(input("De que tamaño será la lista? "))
    objetivo=int(input("Que numero quieres encontrar? "))
    #Crear lista aleatoria del tamaño que dice el usuario y ordenarla lista aleatoria con sorted()
    lista=sorted([random.randint(0,100) for i in range (tamano_De_lista)])


    (encontrado,contador)=busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f"El número de iteraciones con el metodo binario fue {contador}")
    