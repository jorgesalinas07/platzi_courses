class silla_de_ruedas:
    
    def __init__(self, peso_persona, extremidades=4):
        self.peso_persona=peso_persona
        self.extremidades=extremidades
    
    def movimiento_delantero(self, peso_persona):
        if peso_persona>70:
            self._motor(energia=10)
        else:
            self._motor()
        print("Moviendo hacia adelante")

    def dar_comida(self, extremidades):
        if extremidades<4:
            self._mec_alimentacion(extremidades)
        else: 
            self._mec_alimentacion=0
        print("Empezando a dar comida")

    def _mec_alimentacion(self, extremidades):
        pass

    def _motor(self, energia=8):
        pass    

if __name__=="__main__":

    print(silla_de_ruedas(80,3).dar_comida(3))