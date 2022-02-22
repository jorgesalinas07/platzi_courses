
def run():
    LIMITE=1000000;
    contador=0;
    Potencia_2=2**contador
    while Potencia_2<LIMITE:
        print("2 elevado a "+str(contador)+" es igual a: "+str(Potencia_2))
        contador=contador+1
        Potencia_2 = 2**contador;

if __name__=="__main__":
    run()
    contador =1;