from payment import Payment

class debit(Payment):
    cvv=int
    date=int
    number=int

    def __init__(self, id, date, number):
        super().__init__(id)
        self.date=date
        self.number=number