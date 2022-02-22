def productoria(num_prod):
    contador=1
    for i in range(1,num_prod+1):
        contador=contador*i
    return contador

def calculo(numero1):
    dato=numero1-1
    valor=productoria(dato)+1
    return valor

def es_primo(numero2):
    if calculo(numero2) % numero2==0:
        return True
    else:
        return False

def run():
    numero=int(input("Escribe un número: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")

if __name__=="__main__":
    run()