def productoria(num_prod:int)->int:
    contador=1
    for i in range(1,num_prod+1):
        contador=contador*i
    return contador

def calculo(numero1:int)-> int:
    dato=numero1-1
    valor=productoria(dato)+1
    return valor

def es_primo(numero2:int)-> bool:
    if calculo(numero2) % numero2==0:
        return True
    else:
        return False

def run():
    #numero=int(input("Escribe un número: "))
    numero="a"
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")

if __name__=="__main__":
    run()