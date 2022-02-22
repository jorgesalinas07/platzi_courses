class cuenta():
    #1. Inicio Forma inicial
    #Definir clase
    def __init__(self, pro, sal, mon):
        #Definir variables privadas
        self.__propietario=pro
        self.__saldo = sal
        self.__moneda=mon
    #Final forma inicial
    
    #Forma Final

    #Getter (Mostrar un valor oculto)
    #Crear método para mostrar todas las variables ocultas
    def get_saldo(self):
        return self.__saldo
    def get_propietario(self):
        return self.__propietario
    def get_moneda(self):
        return self.__moneda

    #Setter (Modificar un valor oculto)
    #Crear método para modificador el valor del objeto oculto "moneda"
    def set_Moneda(self, moneda):
        self.__moneda=moneda

    #Final forma final
if __name__=="__main__":
    cuenta1=cuenta("Oscar", 150000, "Soles")
    #Inicio forma inicial

    #No permite mostrar el valor en moneda o ninguna porque son variables privadas
    #print(cuenta1.__moneda)
    
    #Fin forma inicial

    #Inicio forma final
    #Usar comando print para mostrar un objeto privado con el método getter
    print(cuenta1.get_saldo())
    #Usar el setter para cambiar el valor de un objeto privado
    cuenta1.set_Moneda("Dolares")
    #Mostrar el valor de moneda para confirmar si cambió
    print(cuenta1.get_moneda())