import random

def ordenamiento_por_mezcla(lista):
    #If para garantizar que no se ha llegado a la divición mas pequeña posible
    if len(lista)>1:
        #Primera parte del codigo tiene como objetivo lograr que la longitud de las listas sea 1
        #Definir la mitad de la lista
        medio=len(lista)//2
        #Definir las primeras divisiones
        izquierda=lista[:medio]
        derecha=lista[medio:]
        print(izquierda, "+" *5, derecha)

        #Crear llamada recursiva en cada mitad para divir cada lista en mas pequeñas
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)
        #Fin de la primera parte. Es de crecimiento logaritmico esta parte
        #Segunda parte del codigo. Empezar a comparar lista pequeña
        #Ubicar los mayores y menores con whiles e ir combinando la parte que ya esta ordenada en las esquinas
        #Iteradores para reccorer las dos listas
        
        i=0
        j=0
        #Iterador para la lista principal
        k=0

        #Usar while con los iteradores para asegurarnos que todavía no han recorrido toda la lista
        while i<len(izquierda) and j<len(derecha):
            #Si se detecta que el miembro i de la primera lista es menor que el miembro j de la segunda, ubicar el numero menor en la lista final y subir el contador de i en uno
            #Si no es menor entonces que ubique directamente el numero mayor en la lista final y sume j en 1 para tomar el siguiente valor
            if izquierda[i]<derecha[j]:
                lista[k]=izquierda[i]
                i+=1
            else:
                lista[k]=derecha[j]
                j+=1
            #Segurarnos que salga del while
            k+=1

        while i<len(izquierda):
            lista[k]=izquierda[i]
            i+=1
            k+=1
        
        while j<len(derecha):
            lista[k]=derecha[j]
            j+=1
            k+=1

        print(f"Izquierda {izquierda}, derecha {derecha}")
        print(lista)
        print("-"*40)
    return lista




if __name__=="__main__":
    #Definir el tamaño
    tamano_De_lista=int(input("De que tamaño será la lista? "))
    #Crear lista aleatoria y mostrarla
    lista=[random.randint(0,100) for i in range(tamano_De_lista)]
    print(lista)
    print("-"*20)
    #ordenar lista y mostrarla
    lista_ordenada=ordenamiento_por_mezcla(lista)
    print(lista_ordenada)