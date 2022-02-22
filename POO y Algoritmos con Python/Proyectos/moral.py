#Se le da la catidad de kg que puede tener el morral
#Se le dan los pesos y los respectivos valores de esos pesos de forma organizada
def morral(tamano_morral,pesos, valores, n):
    #Crear un caso base. No hay mas elemenos o ya se lleno el morral
    print(tamano_morral)
    print(valores)
    if n==0 or tamano_morral==0:
        return 0
    #Si el siguiente elemento es mas grande que el tamaño que tengo disponible, se debe pasar qal siguiente elemento
    if pesos[n-1]>tamano_morral:
        #Crear recursividad para ejecutar la funcion con el siguiente elemento
        return morral(tamano_morral,pesos,valores,n-1)
    #Ahora, hay dos opciones: 
    # primero escoger el elemento siguiente (n) con sus valores y pesos
    #Segundo pasar al siguiente elemento y por lo tanto no tomar el valor y el peso del siguiente
    #La funcion MAX devuelve el valor maximo entre dos valores posibles
    #El primer valor en max es que caso de que si lo tome y el segundo en el que no lo tome
    #Si no lo tomo, solamente esta evaluando el valor del siguiente elemento con n-1
    #Si lo tomo,
    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),morral(tamano_morral, pesos, valores, n - 1))

if __name__=="__main__":
    #El primer objeto pesa 10 kg y tiene un valor de 60 y así
    valores=[60, 100, 120]
    pesos=[10, 20, 30]
    tamano_morral=50
    n=len(valores)
    #Se va a recorrer de adelante hacia atras los valores de n
    resultado=morral(tamano_morral, pesos, valores, n )
    print(resultado)