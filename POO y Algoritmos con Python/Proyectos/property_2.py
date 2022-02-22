class CasillaDeVotacion:
    def __init__(self, indentificador,pais):
        self.__identificador=indentificador
        self.__pais=pais
        self.__region=None
    
    @property
    def region(self):
        return self.__region
    
    @region.setter
    def region(self,region):
        if region in self.__pais:
            self.__region=region
        else:
            raise ValueError(f"La region {region} no es valida en {self.__pais}")
        

casilla=CasillaDeVotacion(123, ["Ciudad de Mexico", "Morelos"])
