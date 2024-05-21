# print('hola mundo')
# print(hola mundo) #error syntax, no se llega a ejecutar nada
# print('hola mundo)



# if True: #error identation
    
    
    
    
# print(2+2)
#---------------------------
#---------------------------
# error semantico, se ejecuta hasta que se rompe

# lista = []

# lista.pop() #error de index (lista vacia)


# True or 4/0


#---------------------------
#---------------------------

# variable + 2 #variable no definida

# print(2+2)
# print(2+2)
# print(2+2)
# print(2+2)
# print(2+2)
# 4/0         #zero division error
# print(2+2)
# print(2+2)


# {}.discard

#---------------------------
#---------------------------


# def dividir(a,b):
#     return a/b

# print(dividir(5,4))


# def dividir(a,b):
#     return a/b

# print(dividir(0,4))

# def dividir(a,b):
#     return a/b

# print(dividir(5,0))  #errrorrrr



# def dividir(a,b):
#     if b == 0:
#         return 'No se puede dividir por cero'
#     return a/b

# print(dividir(5,0))  



# def dividir(a,b):
#     if b == 0:
#         return 'No se puede dividir por cero'
#     elif type(b)!= int:
#         return 'No se puede dividir por algo que no es numerico'
#     return a/b

# print(dividir(5,'a'))  

# def dividir(a,b):
#     if b == 0:
#         return 'No se puede dividir por cero'
#     elif type(b) not in [int, float]:
#         return 'No se puede dividir por algo que no es numerico'
#     return a/b

# print(dividir(5,'a'))  

# def dividir(a,b):
#     if type(b) not in [int, float] or b == 0:
#         return 'No se puede dividir porque el divisor no es corrrrrrrrrrectou'
#     return a/b

# print(dividir(5,'a'))  

# def dividir(a,b):
#     try:
#         return a/b
#     except:
#         return 'No se puede dividir porque el divisor no es corrrrrrrrrrectou'
# # print(dividir(5,'a'))  

# print(dividir(5,1))  

# def dividir(a,b):
#     try:  #sirve para que el codigo pruebe, si funca bien sigue, si no el except hace el resto
#         print(2+2)
#         print(2+2) 
#         print(a/b) 
#         print(2+2) 
#         print(2+2) 
#         print(2+2) 
#         return a/b
#     except:
#         return 'No se puede dividir porque el divisor no es corrrrrrrrrrectou'
# print(dividir(5,'a'))  

# # print(dividir(5,1))  


# def dividir(a,b): #el try de adentro agarra el error, el de afuera no lo va a legar a agarrar
#     try:
#         return a/b
#     except:
#         print('No se puede dividir porque el divisor no es corrrrrrrrrrectou')
#     return 'chinverguencha'

# try:
#     print(dividir(5,'a'))   
# except:
#     print('Mensaje del except de afuera')

# bandera = True
# while bandera:
#     print('''
#           Selecione una opcion:
#           1. Retirar efectivo.
#           2. Cambiar contraseña.          
#           3. Salir.
#           ''')
#     opcion = input('Ingrese la opcion:')
#     if opcion == '1':
#         print('Retirar efectivo')
#     elif opcion == '2':
#         print('Cambiar contraseña')
#     elif opcion == '3':
#         bandera = False
#     else:
#         raise Exception()

# bandera = True
# while bandera:
#     print('''
#           Selecione una opcion:
#           1. Retirar efectivo.
#           2. Cambiar contraseña.          
#           3. Salir.
#           ''')
#     try:
#         opcion = input('Ingrese la opcion:')
#         if opcion == '1':
#             print('Retirar efectivo')
#         elif opcion == '2':
#             print('Cambiar contraseña')
#         elif opcion == '3':
#             bandera = False
#         else:
#             raise Exception()
#     except:
#         print('Ingresaste algo incorrecto. Volve a selecionar una opcion.')

# bandera = True
# while bandera:
#     print('''
#           Selecione una opcion:
#           1. Retirar efectivo.
#           2. Cambiar contraseña.          
#           3. Salir.
#           ''')
#     try:
#         opcion = input('Ingrese la opcion:')
#         if opcion == '1':
#             print('Retirar efectivo')
#         elif opcion == '2':
#             print('Cambiar contraseña')
#         elif opcion == '3':
#             bandera = False
#         else:
#             raise Exception() #----------> va al else de afuera
#     except:
#         print('Ingresaste algo incorrecto. Volve a selecionar una opcion.')
#     else:      #<----------- #este else es del try
#         print('pase por el else')

# bandera = True
# while bandera:
#     print('''
#           Selecione una opcion:
#           1. Retirar efectivo.
#           2. Cambiar contraseña.          
#           3. Salir.
#           ''')
#     try:
#         opcion = input('Ingrese la opcion:')
#         if opcion == '1':
#             print('Retirar efectivo')
#         elif opcion == '2':
#             print('Cambiar contraseña')
#         elif opcion == '3':
#             bandera = False
#         else:
#             raise Exception() #----------> va al else de afuera
#     except:
#         print('Ingresaste algo incorrecto. Volve a selecionar una opcion.')
#     else:      #<-----------
#         print('pase por el else')
#     finally:
#         print('pase por el finally') #pasa siempre indistintamente

#--------------------
#--------------------


# def dividir(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError: # eleccion de error especifico
#         return 'no podes dividir por cero'
#     except TypeError:
#         return 'el tipo no es correcto'
#     except Exception: # eleccion de error generico
#         return 'pase por el except'
    
    
# print(dividir(5,'a'))
# print(dividir(5,0))

def dividir(a,b):
    try:
        return a/b
    except ZeroDivisionError as error: # eleccion de error especifico
        # return f'no podes dividir por cero {error}'
        return f'no podes dividir por cero {type(error).__name__}'
        
    except TypeError as pepito: #as **** guarda en un str
        # return f'el tipo no es correcto {pepito}'
        return f'el tipo no es correcto {type(pepito)}'
    
    except Exception as er: # eleccion de error generico
        # return f'pase por el except {er}'
        return f'pase por el except {type(er)}'
    
# print(dividir(5,'a'))
print(dividir(5,0))
    
    
print(dividir(5,'a'))
print(dividir(5,0))

