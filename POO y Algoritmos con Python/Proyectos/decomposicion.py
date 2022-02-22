class Automovil:

    def __init__(self, modelo, marca,color):
        self.modelo=modelo
        self.marca=marca
        self.color=color
        self._estado="en_reposo"
        self._motor=Motor(cilindros=4)
        self.check=Mantenimiento(filtros=1,aceite=1)

    def acelerar(self,tipo="despacio"):
        if tipo =="rapida":
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado="en_movimiento"

class Motor:
    
    def __init__(self, cilindros, tipo="Gasolina"):
        self.cilindros=cilindros
        self.tipo=tipo
        self._temperatura=0
    
    def inyecta_gasolina(self,cantidad):
        pass

class Mantenimiento:

    def __init__(self, filtros, aceite, frenos="reparados"):
        self.filtros=filtros
        self.aceite=aceite
        self._cant_gasolina= 100

