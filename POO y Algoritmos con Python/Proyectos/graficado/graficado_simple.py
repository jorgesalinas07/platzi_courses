from bokeh.plotting import figure, output_file, show
#Figure -> Ventana donde se grafica
#output_file -> Colocarle nombre al archivo que sale
#show -> Generar un servidor que se enciende y muestra el archivo HTML en el browser

if __name__=="__main__":
    #Colocar nombre de archivo de salida
    output_file("graficado_siemple.html")
    #Lugar donde se genera el grafico. El tipo se mira con type() y help() para saber los métodos
    fig=figure()
    #Pedir el tamaño de la grafica
    total_vals=int((input("Cuantos valores quieres graficar?: ")))
    #Generar los valores de X. list -> Genera una lista
    x_vals=list(range(total_vals))
    y_vals=[]

    for i in x_vals:
        val=int(input(f"Escriba el valor y para la x {i}"))
        y_vals.append(val)
    #Los dos arrays debe ser del mismo tamaño para este tipo de grafica

    #Dar valores a la grafica. (Val x, Val, propiedades separadas por coma)
    fig.line(x_vals,y_vals, line_width=2)

    #Mostrar grafica
    show(fig)