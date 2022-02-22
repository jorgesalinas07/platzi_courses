def run():
    objetivo =int(input("Escribe un numero: "))
    epsilon=0.0001
    paso=epsilon**2
    respuesta=0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(respuesta)
        respuesta+=paso


    if abs(respuesta**2-objetivo)>=epsilon:
        print(f"No se encontró la raíz cuadrada {objetivo}")
    else:
        print(f"La raíz cuadrada de {objetivo} es {respuesta}")



if __name__=="__main__":
    run()