def run():
    nom_persona1=input("Escriba el nombre de la primera persona: ")
    est_persona1=int(input("Escriba la estatura de la primera persona: "))
    nom_persona2=input("Escriba el nombre de la segunda persona: ")
    est_persona2=int(input("Escriba la edad de la segunda persona: "))

    
    if est_persona1>est_persona2:
        print("La persona mas alta es: "+nom_persona1)
    elif est_persona1<est_persona2:
        print("La persona mas alta es: "+nom_persona2)
    else:
        print("Tanto "+nom_persona1+" como "+nom_persona2+" miden lo mismo")



if __name__=="__main__":
    run()