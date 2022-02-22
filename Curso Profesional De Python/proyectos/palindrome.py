def is_palindrome(string:str) -> bool:
    #Borrar espacios para confirmar si es palindromo
    #Despues colocar en minusculas
    string=string.replace(" ","").lower()
    #Confirmar que la palabra es igual al derecho que al revez 
    return string==string[::-1]

def run():
    #Si se le pasa un número en lugar de str da un error de que replace no funciona con str
    #Sin embargo, debería decirnos que la funcion esperaba un str y se le dió un int
    #Para solicionar se debe abrir con mypy así:
    #mypy palindrome.py --check-untyped-defs
    #Esto sirve para ver los errores de tipo
    print(is_palindrome(1000))
    #El resultado dice:
    # palindrome.py:9: error: Argument 1 to "is_palindrome" has incompatible type "int"; expected "str"
    # Found 1 error in 1 file (checked 1 source file)

if __name__=="__main__":
    run()