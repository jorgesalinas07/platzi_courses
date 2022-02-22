from datetime import datetime 
my_day=datetime.today()
print(my_day)
print(f'year: {my_day.year}')
print(f'month: {my_day.month}')
print(f'day: {my_day.day}')

#Mostrar la fecha en un formato en especial
my_datetime=datetime.now()

my_str=my_datetime.strftime('%d/%m/%Y')
print(f'Formato LATAM {my_str}')

my_str=my_datetime.strftime('%m/%d/%Y')
print(f'Formato USA {my_str}')

my_str=my_datetime.strftime('Estamos en el año %Y')
print(f'Formato LATAM {my_str}')

