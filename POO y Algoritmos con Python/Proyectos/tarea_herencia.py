class ArrozBlanco:
    
    def __init__(self, agua=20, arroz=30, aceite=50):
        self.agua=agua
        self.arroz=arroz
        self.aceite=aceite

    def ingredientes(self):
        return [self.agua,self.arroz,self.aceite]
        #print(f"Los ingredientes son {agua} L de agua, {arroz} tazas de arroz, {aceite} cucharadas de aceite")
    
class ArrozDeFideo(ArrozBlanco):
    def __init__(self, fideo):
        super().__init__(agua=20, arroz=30,aceite=50)
        self.fideo=fideo
    
    def ingredientes2(self):
        return [super().ingredientes(),self.fideo]

if __name__=="__main__":
    #print(ArrozBlanco(2,3,4).ingredientes())
    print(ArrozDeFideo(7).ingredientes2())

