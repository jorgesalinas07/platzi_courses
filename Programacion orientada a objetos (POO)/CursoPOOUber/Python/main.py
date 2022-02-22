from car import Car
from account import Account
from UberX import Uberx
from user import user

if __name__=="__main__":
    print("Info de carros")
    car=Car("AMS234", Account("Andres Herrera", "ANDA876"))
    print(vars(car)) 
    print(vars(car.driver))

    print("Uber x")
    Uberx=Uberx("IRS123", Account("JORGE", "SOINV"), "TOYOTA", "2019")
    print(vars(Uberx))
    print(vars(Uberx.driver))

    print("Usuario")
    user=user("Jorge", "droibn")
    print(vars(user))