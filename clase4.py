# # strings

# # metodo upper

# cadena1 = 'soY la pRimer cadena'
# # print(cadena1)
# # cadena1_en_mayusculas= cadena1.upper() #todo.upper muestra en mayuscula todo el string
# # # cadena1= cadena1.upper()
# # print(cadena1)
# # print(cadena1_en_mayusculas)

# # cadena1_en_minusculas = cadena1.lower() #en minusculas
# # print(cadena1_en_minusculas)

# # cadena1_en_modo_titulo = cadena1.title() #cada palabra la empieza en mayuscula
# # print(cadena1_en_modo_titulo)

# # cadena1_parrafo = cadena1.capitalize() #primera letra en mayuscula
# # print(cadena1_parrafo)

# # print(cadena1.count('a')) #sirve para string para contar caracteres/palabras
# # print(cadena1.count(' '))
# # print(cadena1.count('z'))

# # print(cadena1.find('a')) #sirve para string para averiguar el indice de izq a der
# # print(cadena1.find(' '))
# # print(cadena1.find(''))
# # print(cadena1.find('z'))

# # print(cadena1.rfind('a'))# lo mismo pero al revez
# # print(cadena1.rfind(' '))
# # print(cadena1.rfind(''))
# # print(cadena1.rfind('z'))

# # cadena2 = 'segunda cadena al rescate'
# # # lista = ['segunda', 'cadena', 'al', 'rescate']
# # lista = cadena2.split() #separa el string en cada uno de los espacios, separando las palabras
# # print(lista)
# # lista2 = cadena2.split('a')  #recorta segun lo que indiques
# # print(lista2)
# # lista3 = cadena2.split('a ')
# # print(lista3)
# # lista4 = cadena2.split('asd el pepe loco')
# # print(lista4)

# # lista = ['segunda', 'cadena', 'al', 'rescate']
# tupla=('segunda', 'cadena', 'al', 'rescate')
# # cadena = ' '.join(lista)  #une la cadena seoarada a partir de una especie de separador
# # print(cadena)
# # cadena = '<>pepito<>solito<>'.join(lista)
# # print(cadena)
# cadena = '-=-=-'.join(tupla)
# print(cadena)

# password = input('ingrese un password: ') #strip para borrar caracteres en principio y final
# # print(password.strip())
# # print(password)

# print(password.strip('asd'))
# print(password)

# palabra_repetida = 'cadena cadena cadena cadena cadena'
# # palabra_repetida_modificada = palabra_repetida.replace('cadena', 'otra')
# palabra_repetida_modificada = palabra_repetida.replace('cadena', 'otra', 3)
# print(palabra_repetida)
# print(palabra_repetida_modificada)

# lista = ['segunda', 'cadena', 'al', 'rescate']
# print(lista)
# lista.clear()
# print(lista)

# lista2 = lista + [1,2,3]
# print(lista2)

# lista += [1,2,3]
# print(lista)

# lista.extend([1,2,3])
# print(lista)

# lista.insert(0, 'pepitooooo')
# print(lista)

# lista.reverse()
# # lista.reverse() lo mismo que: lista=lista[::-1]
# print(lista)

# lista_numeros = [5,1,2,3,4,10]
# # lista_numeros.sort()
# lista_numeros.sort(reverse=True)
# print(lista_numeros)

# lista_numeros1 = ['5','1','2','3','4','10']
# lista_numeros1.sort()
# # lista_numeros1.sort(reverse=True)
# print(lista_numeros1)

#Sets

# conjunto1 = {1, 'valor1', (1, True)}
# iterable1= (1, 'valor1', (1, True))
# print(conjunto1.isdisjoint(iterable1))
# iterable2 = (2, 'valor2',(2, True))
# print(conjunto1.isdisjoint(iterable2))

# conjunto1 = {1, 'valor1', (1, True)}
# iterable1= (1, 'valor1', (1, True), 45)
# print(conjunto1.issubset(iterable1))

# conjunto1 = {1, 'valor1', (1, True)}
# iterable1= (1, 'valor1', (1, True), 45)
# print(conjunto1.issuperset(iterable1))

# conjunto1 = {1, 'valor1', (1, True)}
# iterable1= (1, 'valor1', (1, True), 45)
# print(conjunto1.difference(iterable1))
# print(conjunto1)

# conjunto1 = {1, 'valor1', (1, True)}
# iterable1= (1, 'valor1', (1, True), 45)
# print(conjunto1.intersection(iterable1))
# variable = conjunto1.intersection(iterable1)
# print(conjunto1)

# conjunto1 = {1, 'valor1', (1, True)}
# iterable1= (1, 'valor1', (1, True), 45)
# print(conjunto1.difference_update(iterable1))
# print(conjunto1)

# conjunto1 = {1, 'valor1', (1, True)}
# iterable1= (1, 'valor1', (1, True), 45)
# conjunto1.intersection_update(iterable1)
# print(conjunto1)

#Dics

# auto = {
#     'motor' : 'v8',
#     'color' : 'negro',
#     'vidrios' : (6, 'blindados'),
#     'pasajeros' : '4',
# }
# valor1 = auto['motor']
# print(valor1)
# # valor2 = auto['ricardo']
# # print(valor2)
# valor3 = auto.get('ricardo', False)
# print(valor3)

#conjuntos

# numero1 = 1
# numero2 = numero1
# numero1 += 2
# print(numero1)
# print(numero2)

# conjunto1 = {1, 'conjunto1', (1, True)}
# conjunto3 = conjunto1
# print(conjunto3)
# conjunto1.add(456)
# print(conjunto3)

# Copy

# conjunto1 = {1, 'conjunto1', (1, True)}
# conjunto3 = conjunto1
# conjunto3 = conjunto1.copy()
# print(conjunto3)
# conjunto1.add(456)
# print(conjunto3)
