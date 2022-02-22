def primera_letra(lista_de_palabras):
    "Función para generar una lista con las primeras letras de una lista con varias palabras"

    primeras_letras=[]

    for palabra in lista_de_palabras:
        try:
            assert type(palabra)==str, f"{palabra} no es string"
            assert len(palabra) >0, "No se permiten str vacios"
        except AssertionError as e:
            print(e)

        primeras_letras.append(palabra[0])

    return primeras_letras

if __name__=="__main__":
    lista1=[]
    print(primera_letra(lista1))