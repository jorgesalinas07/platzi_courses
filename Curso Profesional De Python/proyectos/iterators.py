import time 
"""Crear iterador con la sucesion de fibonachi"""

class FiboIter():

    #No se usará dander init porque no se necesita ningun atributo adicional


    def __iter__(self):
        #Fibonachi va sumando los dos números anteriores
        #porque lo que se crean las variables que contendran los valores iniciales y irán cambiando
        self.n1=0
        self.n2=1
        #Contar cuantas vueltas hace el iterador
        self.counter=0
        #Siempre se debe retornar self
        return self


    def __next__(self):
        #If para la primera vuelta del iterador
        if self.counter==0:
            #Sumar contador porque otra iteración
            self.counter +=1
            #Retornar el primer número (0) porque ese es el valor del primer caso
            return self.n1
        #Hacer un if igual para el caso de la segunda vuelta
        elif self.counter==1:
            self.counter +=1
            return self.n2
        #Hacer un if para el comportamiento regular de la serie (diferente la primera y segunda vuelta)
        else:
            #Aquí se va a ir sumando los dos números anteriores
            self.aux=self.n1+self.n2
            #Después se procede a correr un número a la derecha
            #Primero cambiando el primer valor porque n2
            ##self.n1=self.n2
            #Después cambiando n2 por la suma
            ##self.n2=self.aux

            #Lo se que se acaba de hacer puede ser remplazado por un "swap":
            self.n1,self.n2=self.n2,self.aux
            #Se lee así: el primer elemento antes del igual (self.n1), tendra el valor del primer elemento después del igual (self.n1)
            #Lo mismo pasa con el segundo valor antes y después del igual
            self.counter +=1
            return self.aux


if __name__=="__main__":
    #Aquí solo se inicia la variable con __iter__
    fibonacci=FiboIter()

    #Aquí se ejecuta el __next__
    for element in fibonacci:
        print(element)
        #Pausar para poder ver la suceción. En este caso 1 segundo
        time.sleep(1)