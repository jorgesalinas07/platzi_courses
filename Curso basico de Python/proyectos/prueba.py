def productoria(num_prod):
    contador=1
    for i in range(1,num_prod+1):
        contador=contador*i
    return contador

def run():
    numero=int(input("Escribe un número: "))
    print(productoria(numero))

if __name__=="__main__":
    run()