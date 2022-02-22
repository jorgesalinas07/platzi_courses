from car import Car

class UberBlack(Car):
    typeCarAcepted=[]
    seatsmaterial=[]

    def __init__(self, license, driver, typeCarAcepted, seatsmaterial):
        super().__init__(license, driver)
        self.typeCarAcepted= typeCarAcepted
        self.seatsmaterial = seatsmaterial
