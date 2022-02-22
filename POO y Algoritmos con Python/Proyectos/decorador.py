def funcion_decoradora(funcion):
	def wrapper():
		print("Este es el último mensaje...")
		funcion()
		print("Este es el primer mensaje ;)")
	return wrapper

# def zumbido():
# 	print("Buzzzzzz")


if __name__=="__main__":

    @funcion_decoradora
    def zumbido():
        print("Buzzzzz")

    zumbido()

    # Forma sin decorador
    # zumbido = funcion_decoradora(zumbido)
    # print(zumbido())
