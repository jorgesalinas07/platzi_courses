def factorial(n):
    """Calcula el factoria de n
    n int >0
    return n!
    """
    print(n)
    if n==1:
        return 1
    return n*factorial(n-1)



if __name__=="__main__":

    n=int(input("Escribir el numero para el factorial: "))
    print(f"la respuesta es {factorial(n)}")