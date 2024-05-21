# print(r'c\no_ta_loco\tortita_de_manteca')

# print(r'https://docs.google.com/presentation/d/1lDuvXwi0Pea5cfc0qNaEvw7O3VCx1lohj5BCR0v3_3o/edit#slide=id.p19')

# direccion = input('ingresa la url: ')
# print(direccion)

# import os

# import sys

# print(sys.argv)

# suma = 0
# valores_a_sumar = sys.argv[1:]
# for valor in valores_a_sumar:
#     suma += int(valor)
# # valor1 = int(input('ingresa un valor: '))
# # valor2 = int(input('ingresa otro valor: '))

# print(f'la suma de {sys.argv[1:]}  es {suma}')

#===============================================

# import sys

# print(sys.argv)

# valores = sys.argv[1:]

# if len(valores) == 2:
#     print(f'la suma de {valores[0]} y {valores[1]}' 
#           f'es {int(valores[0])+ int(valores[1])}')
# else:
#     print('no me podes pasar ni mas ni menos de 2 valores numericos')

#===============================================
#===============================================

# def sumar(a,b):
#     return a+b


# def restar(a,b):
#     return a-b
#===============================================
#modulos
# #v1
# import operacion #importacion de modulo de operacion.py

# print(operacion.sumar(2,4)) #argumento adentro de operacion.py
# print(operacion.restar(2,4))

# cuadrado = operacion.Cuadrado(5)
# print(cuadrado.perimetro())

# print(operacion.var_de_operacion)

#===============================================

# #v2
# from operacion import sumar, restar, Cuadrado, var_de_operacion #importacion de modulo de operacion.py

# print(sumar(2,4)) #argumento adentro de operacion.py
# print(restar(2,4))

# cuadrado = Cuadrado(5)
# print(cuadrado.perimetro())

# print(var_de_operacion)

# #===============================================

# #v3
# from operacion import * #importacion de modulo de operacion.py

# print(sumar(2,4)) #argumento adentro de operacion.py
# print(restar(2,4))

# cuadrado = Cuadrado(5)
# print(cuadrado.perimetro())

# print(var_de_operacion)

# #===============================================

# #v4
# from matematica.operacion import sumar as sumar_de_operaciones, restar, Cuadrado, var_de_operacion
# import matematica.otro_paquete #importacion de modulo de operacion.py

# def sumar(): #asi no porque pisa el import, se arregla con lo de sumar as sumar_de_operaciones
#     print('sumo lo que quiero')


# print(sumar_de_operaciones(2,4)) #argumento adentro de operacion.py
# print(restar(2,4))

# cuadrado = Cuadrado(5)
# print(cuadrado.perimetro())

# print(var_de_operacion)

#===============================================

# from matematica.otro_paquete.mensajes import saludo #2
# # import matematica  #1
# # import matematica.otro_paquete
# # import matematica.otro_paquete.mensajes

# # matematica.otro_paquete.mensajes.saludo() #1
# saludo() #2

#===============================================
#===============================================
# paquetes redistribuibles

# para crearlo hacer un setup.py en la misma altura de la carpeta, 
# #en terminal: py setup.py sdist para crear el paquete
# from matematica.operacion import sumar
# print(sumar(2,2))



#===============================================
