#Crear sets, no se puede acceder a los valores por sus indices
my_set={3,4,5}
print('my_set = ', my_set)

#Crear otro set. En este se podrían imprimir los valor en desorden por que es una colección
my_set2={'Hola', 23.3, False, True}
print('my_set2 = ', my_set2)

#Este set tiene un valor repetido. Python borra el valor repetido porque interpreta que no son importantes estos valores
my_set3={3,3,2}

#Este set dará un error porque la lista es elemento mutable
my_set4={[1,2,3],4}
print('my_set4 = ', my_set4)

#Si quiero crear un set vacio:
empty_set=set()
print(type(empty_set))

#NO:
empty_set={}
print(type(empty_set))

#Convertir lista a set
my_list=[1,1,2,3,4,4,5]
my_set=set(my_list)
print(my_set)

#Convertir tupla a set
my_tuple=('Hola','Hola', 'Hola',1)
my_set2=set(my_tuple)
print(my_set2)

#Agregar valores a un set
my_set={1,2,3}
print(my_set)

my_set.add(4)
print(my_set)

#Añadir varios elementos a un set
#El método update solo añade los valores que no estén ya en el set
#En este caso el 1 y 2 ya estaban así que no los añade
my_set.update([1,2,5])
print(my_set)

#Añadir varias estructuras de dato
#En este caso, se añade una tupla y un set
my_set.update((1,7,2), {6,8})
print(my_set)

#Para borrar elementos del set se usa remove y discard
my_set={1,2,3,4,5,6,7}
print(my_set)

#Borrar un elemento existente. Borrar el 1 funciona igual para ambos métodos
my_set.discard(1)
print(my_set)

my_set.remove(2)
print(my_set)

#Borrar un elemento inexistente. Discard solo retorna el mismo set. Remove levanta un error
my_set.discard(10)
print(my_set)

my_set.remove(12)
print(my_set)

#Borrar elemento aleatorio
my_set.pop()
print(my_set)

#Borrar todos los elementos del set
my_set.clear()
print(my_set)