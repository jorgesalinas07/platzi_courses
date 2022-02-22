#def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    #  for i in range(10000):
    #      print(i)
    #      if i==2352:
    #          break
    # texto=input("Escribe un texto: ")
    # for letra in texto:
    #     if letra=="o":
    #         break
    #     print(letra) 

    
# def run():
contador=0
LIMITE=1000
while contador < LIMITE:
    if contador % 2 != 0:
        contador=contador+1
        continue
    if contador==998:
        break
    contador=contador+1
    print(contador)
                
# if __name__=="__main__":
#     run()