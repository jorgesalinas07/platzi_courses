import time 
"""Crear iterador con la sucesion de fibonachi"""

class FiboIter():

    #No se usará dander init porque no se necesita ningun atributo adicional

    def __init__(self, max=None):
        self.max=max

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
            self.aux=0
            return self.n2
        #Hacer un if para el comportamiento regular de la serie (diferente la primera y segunda vuelta)
        else:
            if self.max==None:
                self.aux=self.n1+self.n2
                self.n1,self.n2=self.n2,self.aux
                self.counter +=1
                return self.aux

            if self.max!=None:
                if self.counter<=self.max:
                    self.aux=self.n1+self.n2
                    self.n1,self.n2=self.n2,self.aux
                    self.counter +=1
                    if self.aux <= self.max:
                        return self.aux
                    else:
                        raise StopIteration


if __name__=="__main__":
    #Aquí solo se inicia la variable con __iter__
    fibonacci=FiboIter(10)

    #Aquí se ejecuta el __next__
    for element in fibonacci:
        print(element)
        #Pausar para poder ver la suceción. En este caso 1 segundo
        time.sleep(0.5)