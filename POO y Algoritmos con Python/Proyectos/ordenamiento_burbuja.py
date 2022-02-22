import random
#Algoritmo con complejidad O(n**2). Es inestable con tamaños de lista grandes
def ordenamiento_de_burbuja(lista):
    #Calcular tamaño de la lista
    n=len(lista)
    #Iniciar dos for para recorrer la lista n veces y por cada ves mover el mayor a la derecha cada vez mas
    for i in range(n):
        #El rango del segundo for es así para evitar redundancia dado que al mover los mayores a la derecha, hace innecesario analizar esos números. Se puede hacer con solo n
        for j in range(0,n - i - 1):
            #Si encuenta un numero mayor a la derecha, cambia los lugares
            if lista[j]>lista[j+1]:
                #swap echo con sintaxis de python
                lista[j], lista[j+1]=lista[j+1],lista[j]
    return lista
if __name__=="__main__":
    #Definir el tamaño
    tamano_De_lista=int(input("De que tamaño será la lista? "))
    #Crear lista aleatoria y mostrarla
    lista=[random.randint(0,100) for i in range(tamano_De_lista)]
    print(lista)
    #ordenar lista y mostrarla
    lista_ordenada=ordenamiento_de_burbuja(lista)
    print(lista_ordenada)