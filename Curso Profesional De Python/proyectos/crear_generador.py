#Los generadores son sugar sintax de los iteradores
#Se crean con funciones en lugar de clases

def my_gen():

    """Un ejemplo de generadores"""
    #Imprime algo y crea variable n de scope locar
    print('Hello World')
    n=0
    #keyword parecido a return con la diferencia que en lugar de detener la funcion la para pausa
    #Retorna n y se pausa la función
    yield n

    #Así sucede con los demas

    print('Hello heaven')
    n=1
    yield n

    print('Hello hell')
    n=2
    yield n

#Se debe iniciar un objeto que guarde el resultado de la función
a=my_gen()
#En este caso, la función next ejecutará el yield mas cercano
print(next(a))  #Hello world
print(next(a))  #Hello heaven
print(next(a))  #Hello hell
#Cuando no quedan mas yields, se ejecuta un StopIterations
print(next(a))  #StopIteration
