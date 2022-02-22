"""Platzigram views"""
#Borrar todo porque se puede ahcer con autentication de django
# #Se debe importar para la respues de http
# from django.http import HttpResponse
# #Utilities
# from datetime import datetime
# #Importar modulo para poder dar una respuesta de diccionario en formato json
# import json


# def hello_world(request):
#     """Return a greeting"""
#     #Colocar fecha en formato especifico 
#     now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
#     #Enviar la fecha al servidor e identificar que now es str. 
#     return HttpResponse('Oh, hi! Current server time is {now}'.format(now=str(now)))


# def hi(request):
#     """Hi"""
#     #Mostrar la instancia creada de https en el runserver
#     # Para este caso se muestra <WSGIRequest: GET '/hi/'>
#     # Significa que es una wsgirequest con el método GET y la url fue '/hi/' 
#     #Se puede imprmir cualquier atributo dependiendo del método usado (Mirar documentación para mas métodos)
#     #print(request)

#     #Hacer esto para cada atributo puede ser tedioso por lo que se usa la herramienta:
#     #Este crea un debugger en la consola cada que se ejecute el código
#     #En la consola se puede acceder a los atributos con los métodos igual que los anteriores (Mirar documentación para mas métodos)
#     #import pdb; pdb.set_trace()
#     #Http response sirve para enviar una respuesta al servidor
#     return HttpResponse("Hi!")


# def sort(request):

#     #Para devolver una lista de numeros ordenada:
#     # numbers=[int(i) for i in  request.GET['numbers'].split(',')]
#     # sorted_ints=sorted(numbers)
#     # return HttpResponse(str(sorted_ints),content_type='application/json')
#     #Para devolver la lista de numeros ordenada en un diccionario
#     numbers=[int(i) for i in  request.GET['numbers'].split(',')]
#     sorted_ints=sorted(numbers)
#     data={
#         'status':'ok',
#         'numbers':sorted_ints,
#         'message':'Integers sorted successfully'
#     }
    
#     return HttpResponse(
#         json.dumps(data,indent=4), 
#         content_type='application/json'
#         )

# #La segunda cosa que agrega django son los argumentos requeridos
# #En este caso, se declaró que se requerián las variables name y age así estás se pasan
# def say_hi(request, name, age):
#     if age<12:
#         message='Sorry {}, you are not allowed here'.format(name)
#     else:
#         message='Hello, {}! Welcome to platzigram'.format(name)

#     return HttpResponse(message)