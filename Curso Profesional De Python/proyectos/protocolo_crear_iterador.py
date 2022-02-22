#Para crear un iterador se debe crear una clase
#con los métodos __iter__ y __next__.

class EvenNumbers:

    """Clase que implementa un iterador de todos los
    números pares, o los números pares hasta un maximo"""

#Definir metodo init para el número maximo de primos a los que llegara
def __init__(self, max=None):
    self.max=max

#iter es Método para  tomar los elemento necesario para que el iterador funcione
#En este caso, los elementos necesarios son lo números de la iteracion
#Se inicializa el elemento necesario (en este caso empezamos con el primer número primo que es 0)
#Y despues retornamos el mismo valor para tenerlo disponible para después
def __iter__(self):
    self.num=0
    return self

#next es Método para extraer los elementos del iterador
#En este caso, se van a extraer todos los números pares
#Ó todos los números pares hasta lo máximo
#El método ira tomando los valores primos
def __next__(self):
    #Definir los limites en los cuales va a funcionar el iterados
    #En este caso, los limites son cuando no se definio un maximo (busqueda infinita de primos)
    #Ó cuando no se haya llegado al limite
    if not self.max or self.num <= self.max:
        #Tomar el número primo actual con result
        result=self.num
        #Cada dos números hay un primo, por eso se va tomando de dos en dos
        self.num+=2
        #Retornar el número primo actual tomado
        return result
    else:
        raise StopIteration

#El algoritmo empezará en 0 e irá sumando de dos en dos hasta el infinito
#teniendo en cuenta todos los primos. Si se le define un maximo, solo llega hasta ahí