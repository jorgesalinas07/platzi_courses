def run():
    nombre=input("Escriba su nombre: ")
    saludo=f"Hola {nombre}, un gusto en conocerte."
    letras=len(saludo)
    print("Hola "+nombre+", un gusto en conocerte. La loguitud del saludo es "+str(letras))

if __name__=="__main__":
        run()