#Crear la lista
my_list=[1,2,3,4,5]
#Convertir a iterador
my_iter=iter(my_list)

#Usar while para ciclo infinito con true=true
#Solo saldra cuando se llegue al ultimo elemento, es decir, levate el error stopiterations

while True:
    try:
        element=next(my_iter)
        print(element)
    except StopIteration:
        break

#For es un alias que hace lo mismo:

for element in my_list:
    print(element)