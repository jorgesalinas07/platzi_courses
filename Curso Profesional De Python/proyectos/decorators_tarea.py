def decorador(func):

    def wrapper(*args,**kargs):
        func(*args,**kargs)
        cantidad=args[0]
        porcetaje=args[1]/100
        calculo=(cantidad*porcetaje)*12
        print(f"El fondo de inversión que tendrías en un año sería: {calculo}")
    return wrapper

@decorador
def fondo_inversion(cantidad:int, porcetaje:int):
    print(f"Si ahorras el {porcetaje} por ciento de tu salario de {cantidad}")

if __name__=="__main__":
    fondo_inversion(2500000,10)