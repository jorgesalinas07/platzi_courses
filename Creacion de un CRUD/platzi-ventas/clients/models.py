import uuid


class Client:

    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        # Si nos dan id lo usamos. Sino, se el modulo uuid para generar id para garantizar que los id son unicos
        #Si no pasan uid, entonces es node que python lo interpreta como Flase, por eso se usa or
        self.uid = uid or uuid.uuid4()

    def to_dict(self):
        #Vars es función global que accede a una representación de diccionario de la información que se acaba de crear
        return vars(self)

    #Este decorar ejecuta una función sin necesidad que se use una instancia de clase, por eso no se usa self
    @staticmethod
    def schema():
        #Representación de columnas
        return ['name', 'company', 'email', 'position', 'uid']
