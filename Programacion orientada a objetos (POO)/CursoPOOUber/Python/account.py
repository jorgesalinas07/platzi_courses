class Account:
    id = int
    id = str
    name = str
    document = str
    email = str
    password = str

    def __init__(self, name, document):
        self.name=name
        self.document=document