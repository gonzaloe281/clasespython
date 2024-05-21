# clase anterior

# if <condicion>:
#     <bloque de codigo>

# elif <condicion>:
#     <bloque de codigo>

# else <condicion>:
#     <bloque de codigo>

# sentencia <condicion>:
#     <bloque de codigo>
# -------------------------------------------


# while True:
# while []: # -> bool([]) == False

# while [1,2,'pepe']: # -> bool([]) == True
#     <bloque de codigo>

# contador = 0
# while True:
#     contador += 1
#     print('Estoy mostrando este mensaje numero:', contador)


# while False:
#     contador += 1 #Ingnorado por la condicion False
#     print('Estoy mostrando este mensaje numero:', contador)

# contador = 0
# dato_de_condicion = 5
# while dato_de_condicion > 0:
#     contador += 1
#     print('Estoy mostrando este mensaje numero:', contador)
#     dato_de_condicion -= 1
    
# print('Ultimo mensaje de mi proyecto')

# contador = 0
# dato_de_condicion = True
# while dato_de_condicion:
#     contador += 1
#     print('Estoy mostrando este mensaje numero:', contador)
#     if contador == 15:
#         dato_de_condicion = False
    # 15 mensajes en terminal
# print('Ultimo mensaje de mi proyecto')

# contador = 0
# dato_de_condicion = True
# while dato_de_condicion:
#     if contador == 15:
#         dato_de_condicion = False
#     contador += 1
#     print('Estoy mostrando este mensaje numero:', contador)
#     # 16 mensajes en terminal (usar el de arriba con if luego del print)
    
# print('Ultimo mensaje de mi proyecto')

# contador = 0
# dato_de_condicion = 2
# while dato_de_condicion:
#     contador += 1
#     print('Estoy mostrando este mensaje numero:', contador)
#     dato_de_condicion -= 1
    
# print('Ultimo mensaje de mi proyecto')

# pass #palabra reservada, simula codigo


#pass
# if 2 >0:
#     pass 
#     ...

# contador = 0
# dato_de_condicion = 0
# while dato_de_condicion:
#     contador += 1
#     print('estoy mostrando un mensaje:', contador)
#     dato_de_condicion -= 1
# else: #se va a ejecutar cuando el while termine correctamente
#     print('pase por else')
    
    
# print('fin de mensajes')


#continue / saltea toda la interacion posterior 

# contador = 0
# dato_de_condicion = 2
# while dato_de_condicion:
#     contador += 1
#     print('estoy mostrando un mensaje:', contador)
#     continue
#     dato_de_condicion -= 1
# else: #se va a ejecutar cuando el while termine correctamente
#     print('pase por else')
    
    
# print('fin de mensajes')

# contador = 0
# dato_de_condicion = 0
# while contador <5:
#     contador += 1
#     if contador == 2:
#         continue
#     print('estoy mostrando un mensaje:', contador)
    
# else: #se va a ejecutar cuando el while termine correctamente
#     print('pase por else')
    
    
# print('fin de mensajes')




#break, frena y saltea todo el bucle y sigue con el otro codigo por afuera del mismo
# contador = 0
# dato_de_condicion = 0
# while contador <5:
#     contador += 1
#     if contador < 2:
#         print('pepito')
#     else:
#         break
        
#     print('estoy mostrando un mensaje:', contador)
    
# else: #se va a ejecutar cuando el while termine correctamente
#     print('pase por else')
    
# print('fin de mensajes')


# lista= [1,2,3,4, 'pepito', True, ('eaea', 'pepe'), 'ochentoso'] #se mantiene un orden
# lista= {1,2,3,4, 'pepito', True, ('eaea', 'pepe'), 'ochentoso'} #un orden al azar / es una bolsa de datos, una vez ya guardado/ejecutado mantiene ese orden (solo en esa ejecucion)

# lista = []
# print('La lista contiene el valor:', lista [0])
# print('La lista contiene el valor:', lista [1])

# indice = 0
# cant_de_elementos = len(lista)
# while indice < cant_de_elementos:
#     print('La lista contiene el valor', lista[indice])
#     indice += 1
    
# for elemento in lista: #en vez de usar una condicion usa una variable para hacer lo mismo que el ejemplo de arriba
#     print('La lista contiene el valor', elemento)

# print('fin de mensajes')


# diccionario = {
#     'marca': 'Ford',
#     'modelo': 'k',
#     'ruedas': '5',
    
# }

# for algo in diccionario.keys():
#     print('El diccionario contiene:', algo) #llaves 'marca...'
    
# for algo in diccionario.values():
#     print('El diccionario contiene:', algo) # valores 'ford...'
    
# for algo in diccionario.items():
#     print('El diccionario contiene:', algo) # items 'marca','ford'....


# dato1, dato2 = ['elemento1', 'elemento2']
# for variable1, variable2 in diccionario.items():
#     print(f'{variable1}: {variable2}')
    
# for key, value in diccionario.items():
#     print(f'{key}: {value}') 


# lista= [1,2,3,4, 'pepito', True, ('eaea', 'pepe'), 'ochentoso'] #se mantiene un orden
# for valor in lista:
#     if valor =='pepito':
#         continue
#     if valor == ('eaea', 'pepe'):
#         break
#     pass
#     ...
#     print('La lista contiene el valor', valor)
# else:
#     print('mostre el else')
    


# enumerate
# range


# lista = [1,2,3,4,5,6,7,8,9]

# for valor in lista:
#     print(valor * 2)
    
# range(500) #arranca esde 1 menos osea 499
# rango = range(1,12)
# lista = [1,2,3,4,5,6,7,8,9]
# # print(type(rango))
# lista_de_rango = list(rango)
# print(type(lista_de_rango))
# # print(type(lista))

# # for valor in lista_de_rango:
# #     print(valor * 2)
    
    
# for valor in range(1,12, 2):
#     print(valor * 2)

# cadena = 'hola soy yo, vos quien sos?'

# indice = 0
# for letra in cadena:
#     print(f'La letra: {letra} ocupa el indice {indice}')
#     indice +=1

# cadena = 'hola soy yo, vos quien sos?'

# indice = 0
# for indice, letra in enumerate(cadena):
#     print(f'La letra: {letra} ocupa el indice {indice}')

lista = [1,2,3,4,5,6,7,8,9,10,11]

for indice, numero in enumerate(lista):
    print(f'El numero: {numero} ocupa el indice {indice}')
