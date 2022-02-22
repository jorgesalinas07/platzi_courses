def desicion(objetivo,desicion):
    if desicion==1:
        respuesta=0
        while respuesta**2<objetivo:
            respuesta += 1
        return(respuesta)


    if desicion==2:
        epsilon=0.01
        paso=epsilon**2
        respuesta=0.0

        while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
            respuesta+=paso

        return(respuesta)

    if desicion==3:
        epsilon=0.01
        bajo=0.0
        alto=max(1.0,objetivo)
        respuesta=(alto+bajo)/2

        while abs(respuesta**2-objetivo)>=epsilon:
            if respuesta**2<objetivo:
                bajo=respuesta
            else:
                alto=respuesta
            respuesta=(alto+bajo)/2
        return(respuesta)
    



def run():
    opcion=int(input("""
    Escoga el metodo para la raíz cuadrada:
    1. Basico.
    2. Epsilon.
    3. Busqueda binaria.
    """))
    numero=int(input("Escriba el numero para la raíz cuadrada: "))
    if opcion==1:
        entrega=desicion(numero,opcion)
        if entrega**2==numero:
            print(f"La raíz cuadrada de {numero} por el metodo 1 es {entrega}")
        else:
            print(f"{numero} no tiene una raíz cuadrada exacta por el metodo 1")


    if opcion==2:
        epsilon=0.01
        entrega=desicion(numero,opcion)
        if abs(entrega**2-numero)>=epsilon:
            print(f"No se encontró la raíz cuadrada de {numero} por el metodo 2")
        else:
            print(f"La raíz cuadrada de {numero} por el metodo 2 es {entrega}")


    if opcion==3:
        entrega=desicion(numero,opcion)
        print(f"La raíz cuadrada de {numero} por el metodo 3 es {entrega}")


if __name__=="__main__":
    run()