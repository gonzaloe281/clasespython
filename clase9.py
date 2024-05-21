# def suma(num1, num2):
#     return num1 + num2

# print(suma(1,2))
# print(suma(2,1))


# def resta(num1, num2):
#     return num1 - num2

# print(resta(1,2))
# print(resta(2,1))


# def resta(num1, num2):
#     return num1 - num2

# print(resta(1,2))
# print(resta(num2=2,num1=1)) #no importa el orden, se asigna valor al nombre

# def resta(num1, num2):
#     return num1 - num2

# print(resta(1,2))
# print(resta(1, num2=2)) #no importa el orden, se asigna valor al nombre
# print(resta(2, num1=1)) #error, multiples valores para el mismo argumento
# print(resta(num2=2, 1)) #error, despues de 1 por nombre, los demas tienen que ir por nombre




# def devuelva_iterable(var1,var2,var3,var4,var5):
#     return var1,var2,var3,var4,var5

# print(devuelva_iterable(1,2,3,4,5))
# print(devuelva_iterable(4,3,1,5,2))
# print(devuelva_iterable(var4=4,var3=3,var1=1,var5=5,var2=2))
# print(devuelva_iterable(1,2,3,var5=5,var4=4))
# print(devuelva_iterable(var2=2,var4=4,3,1,5))
# print(devuelva_iterable(var2=2,3,4,var1=1,5))
# print(devuelva_iterable(1,2,4,var3=3))
# print(devuelva_iterable(1,2,4,var4=3))
# print(devuelva_iterable())


# def devuelva_iterable(var1=10,var2=20,var3=30,var4=40,var5=50):
#     return var1,var2,var3,var4,var5


# print(devuelva_iterable(1,2,3,4,5))
# print(devuelva_iterable(1,2,3,4))
# print(devuelva_iterable(1,2))
# print(devuelva_iterable())

# print(devuelva_iterable(15, var4=255))
# print(devuelva_iterable(var3=255))
# print(devuelva_iterable(var5='soy el cinco', var2=True))



# def saludo():
#     print(pepe)

# saludo() #rompe porque pepe no esta definido

# variable_prueba= 'pepe' #2##: asignado a memoria, no importa si esta antes o despues del def, pero si antes de la llamada

# def saludo(): #1: lee esta linea
    # print(variable_prueba) #no lee, porque define la linea del def(osea esta la info de la def)

# variable_prueba= 'pepe' #2: lee esta linea

# saludo() #usa variable de afuera, clase anterior ##3: ejecuta esta linea con la def (linea1) luego de haber leido lo anterior con su dato
# variable_prueba= 'pepe' #2###: al estar atras de la llamada rompe, por no estar la variable en memoria



# def saludo(): #1: lee esta linea
#     # print(variable_prueba) #rompe porque no asigna lo de afuera al dar la vuelta en la llamada
#     print(variable_prueba) #no lee, porque define la linea del def(osea esta la info de la def)
#     variable_prueba= 'otro gato'# ya valio pepe

# variable_prueba= 'pepe' #2: lee esta linea

# print(variable_prueba) #no lee, porque define la linea del def(osea esta la info de la def)
# saludo() #usa variable 
# print(variable_prueba) #no lee, porque define la linea del def(osea esta la info de la def)


# def saludo(): #1: lee esta linea
#     # print(variable_prueba) #rompe porque no asigna lo de afuera al dar la vuelta en la llamada
#     variable_prueba= 'otro gato'# ya valio pepe
#     print(variable_prueba) #no lee, porque define la linea del def(osea esta la info de la def)
#     return variable_prueba

# variable_prueba= 'pepe' #2: lee esta linea

# print(variable_prueba) #no lee, porque define la linea del def(osea esta la info de la def)
# variable_prueba =  saludo() #usa variable 
# print(variable_prueba) #no lee, porque define la linea del def(osea esta la info de la def)

# def saludo(): #1: lee esta linea
#     global variable_prueba #intentar no usar
#     # print(variable_prueba) #rompe porque no asigna lo de afuera al dar la vuelta en la llamada
#     variable_prueba= 'otro gato'# ya valio pepe
#     print(variable_prueba) #no lee, porque define la linea del def(osea esta la info de la def)
#     # return variable_prueba

# variable_prueba= 'pepe' #2: lee esta linea

# print(variable_prueba) #no lee, porque define la linea del def(osea esta la info de la def)
# saludo() #usa variable 
# # variable_prueba =  saludo() #usa variable 
# print(variable_prueba) #no lee, porque define la linea del def(osea esta la info de la def)

# def actualizacion_de_dato(parametro):
#     parametro = 5

# dato= 2


# print(dato)
# actualizacion_de_dato(dato)
# print(dato)


# def actualizacion_de_dato(parametro):
#     parametro = 'tres'

# dato= 'asd'


# print(dato)
# actualizacion_de_dato(dato)
# print(dato)

# def actualizacion_de_dato(parametro):
#     parametro.append(True) #toca lo de afuera

# dato= [1,2,3,'pepito']


# print(dato)
# actualizacion_de_dato(dato)
# print(dato)

# def actualizacion_de_dato(parametro):
#     parametro.append(True) 

# dato= [1,2,3,'pepito']


# print(dato)
# actualizacion_de_dato(dato.copy()) #no modifica lo de afuera, hace una copia de "dato"
# print(dato)








# *args y **kwargs

# def suma(*args):
#     # print(type(args))
#     # print(args)
#     suma = 0
#     for valor in args:
#         suma += valor
#     return suma
    
    
# print(suma(1,2, 4,3,3,54,2,2,3,34,23,4))


# def suma(*args):
#     # print(type(args))
#     # print(args)
#     suma = []
#     for valor in args:
#         suma += valor
#     return suma
    
    
# print(suma([1,2, 4,],[3,3,54],[2,2,3,34],[23,4])) #concatena las listas en el print



# print('pepe fort de fue de viaje')
# print('pepe', 'fort', 'de', 'fue', 'de', 'viaje')
# print('pepe', 'fort', 'de', 'fue', 'de', 'viaje', sep=',')
# print('pepe', 'fort', 'de', 'fue', 'de', 'viaje', sep='\n')#para entender el *args hace lo mismo que todo esto




# def mostrar(**kwargs):#muestra como diccionario
#     print(type(kwargs))
#     print(kwargs)
#     for llave, valor in kwargs.items():
#         print(f'llave: {llave} --> valor: {valor}')
    
# mostrar(nombre='Pepito', apellido='Grillo')# {llave:valor}
    


def prueba_multiples_parametros(numero, *args,**kwargs):
    print(numero)
    print(args)
    print(kwargs)
    
prueba_multiples_parametros(15,26,True,-29391,'pepito', marca='Ford', kilometros= 24) 
# agarra primero el 15 por numero por posicion
# del 26 a pepito por args
# marca y kilometro como kwargs