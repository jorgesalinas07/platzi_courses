from arreglo import Arreglo
import random
menu = Arreglo(5)
for i in range(len(menu)):
    menu[i] = i+1
print(menu)
print(menu.__replaceitems__())
print(random.randint(1,100))
print(menu.__sumarray__())