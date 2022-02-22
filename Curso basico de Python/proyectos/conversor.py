def calculo(nacion, valor):
    pesos = input("¿Cuantos pesos " + nacion + " tienes?: ")
    pesos = float(pesos);
    valor_dolar = valor;
    dolares = pesos / valor_dolar;
    dolares = round(dolares, 2);
    dolares = str(dolares);  
    print("Tienes $"+ dolares + " dolares.");

menu="""
Bienvenido al conversor de monedas!

1 - Pesos Colombianos.
2 - Pesos Argentinos.
3 - Pesos Mexicanos.

Elige una opción: """

opcion=int(input(menu));

if opcion == 1:
    calculo("Colombianos", 3919);

elif opcion ==2:
    
    calculo("Argentinos", 100);

elif opcion ==3:
    
    calculo("mexicano", 20);

else:
    print("Ingresa una opción correcta por favor")


