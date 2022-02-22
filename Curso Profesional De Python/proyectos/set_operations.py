my_set1={1,2,5}
my_set2={5,6,7}
#Union
my_set3=my_set1 | my_set2
#Resultado: {3,4,5,6,7}
#Itercepción
my_set3=my_set1 & my_set2
#Resultado: {5}
#Diferencia
my_set3=my_set1-my_set2
#Resultado {3,4}
my_set3=my_set2-my_set1
#Resultado {6,7}
#Diferencia asimetrica (Contrario a la intercepción)
#Me quedo con los elementos que no se comparten en ambos
#Me quedo con los elementos de ambos sets menos los que se repiten
my_set3=my_set1 ^ my_set2
#Resultado {3,4,6,7}