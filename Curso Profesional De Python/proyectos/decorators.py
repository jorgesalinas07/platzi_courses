#Importar modulo para trabajar con fechas
from datetime import datetime

#Crear decorar para averiguar cuando tiempo tarda en ejecutarse una función
def execution_time(func):
    #Se crea la funcion wrapper para la ejecucion
    #*args y *kargs sirven para que la funcion se ejecute independiente de el tipo de argumento que se le de a la función
    #Es decir, se le pueden dar varios argumentos y de cualquier tipo (str, int...)
    def wrapper(*args,**kargs):
        #Calcular el momento actual
        initial_time=datetime.now()
        func(*args,**kargs)
        final_time=datetime.now()
        time_elapsed=final_time-initial_time
        #Cantidad de segundos se usa con .total_seconds()
        #Se debe colocar el tiempo en segundos como un string porque solo se puede concatenar string con string
        print("Pasaron "+str(time_elapsed.total_seconds())+" segundos")
    #Retornar funcion para usar el closure
    return wrapper

@execution_time
def random_func():
    #Cuando no interesa la variable en cada vuelta del for, se suele colocar un "_"
    for _ in range(1,100000000):
        pass

@execution_time
def suma(a:int,b:int)->int:
    return a+b

@execution_time
def saludo(nombre="Cesar"):
    print("Hola" + nombre)


if __name__=="__main__":
    random_func()
    suma(5,5)
    saludo("Jorge")