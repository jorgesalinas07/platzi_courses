def make_repeater_of(frase):

    def numero(n:int):
        assert type(frase)==str, "Solo puedes utilizar cadenas"
        print(frase*n)
    
    return numero

def run():
    registro_palabra=input("Escriba la palabra a replicar: ")
    repeticion=make_repeater_of(registro_palabra)
    cuenta=int(input("Escriba el número de veces a repetir: "))
    print(repeticion(cuenta))

if __name__=="__main__":
    run()