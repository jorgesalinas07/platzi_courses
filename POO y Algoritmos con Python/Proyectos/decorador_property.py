class Empleado:
    #Inicio de forma inicial
    #Método constructor con un atributo oculto y otro privado
    def __init__(self,nombre,clave):
        self.nombre=nombre
        self.__clave=clave
    
    #Getter para acceder a atributo privado
    # def getclave(self):
    #     return self.__clave

    #Final de forma inicial

    #Inicio de forma final
    #Crear la propiedad con @property de un método
    @property
    def key(self):
        return self.__clave
    
    #Crear propiedad de setter para modificar valor en atributo privado
    @key.setter
    def key(self, value):
        self.__clave=value


if __name__=="__main__":
    #Inicio forma inicial
    #Crear objeto con la clase EMPLEADO
    em=Empleado("Adan", "osrngvs")
    #Mostrar los atributos del objeto usando el método Getter para el atributo oculto
    # print(em.nombre)
    # print(em.getclave())
    #Fin de forma inicial
    #Inicio de forma final
    #Mostrar atributos con property
    print(em.nombre)
    print(em.key)
    #Utiizar setter para modificar valor
    #Se invoca el setter y getter solo con "key" por que a ambos se les puso el mismo nombre
    #Se activa setter cuando cambiamos la clave y se activa getter cuando mostramos la clave
    em.key="dñjbn"
    print(em.key)