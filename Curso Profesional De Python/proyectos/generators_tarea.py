import time

"""Crear sucesión de fibonacci con generators"""
"""Explicación mas detallada en -iterators-"""
#Como son generadores, se crean funciones en lugar de clases
#Iniciar generador
def fio_gen(max=None):
    #Iniciar variables necesarias
    n1=0
    n2=1
    counter=0

    #Iniciar ciclo infinito
    while True:
        #Caso de primera vuelta: suma al contador y devuelve n1
        if counter==0:
            counter+=1
            yield n1
        #Caso de segunda vuelta: suma al contador y devuelve n2
        elif counter==1:
            counter+=1
            aux=0
            yield n2
        #Vueltas restantes
        else:
            if max==None:
                aux=n1+n2
                #Hacer el swap de valores para correrse a la derecha
                n1,n2=n2,aux
                #Sumar el conteo de vuelta
                counter +=1
                yield aux
            elif max!=None:
                if aux<=max:
                    aux=n1+n2
                    #Hacer el swap de valores para correrse a la derecha
                    n1,n2=n2,aux
                    #Sumar el conteo de vuelta
                    counter +=1
                    if aux<=max:
                        yield aux
                    else:
                        break
        


if __name__=="__main__":
    fibonacci=fio_gen(4)

    for element in fibonacci:
        print(element)
        time.sleep(0.5)