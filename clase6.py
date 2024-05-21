# esta_lloviendo = input('Esta lloviendo??: ')
#  solo if
# if esta_lloviendo == 'si':
#     print('Pase por la sentencia IF')
#     print('Entonces voy a usar paraguas cuando salga.')

# print('mi programa termino')



#if -else
# esta_lloviendo = input('Esta lloviendo??: ')

# if esta_lloviendo == 'si':
#     print('Pase por la sentencia IF')
#     print('Entonces voy a usar paraguas cuando salga.')
# else:
#     print('Pase por la sentencia IF')
#     print('Entonces no voy a usar paraguas cuando salga.')

# print('mi programa termino')

# # if - elif - else
# esta_lloviendo = input('Esta lloviendo??: ').lower()

# if esta_lloviendo == 'si':
#     print('Entonces voy a usar paraguas cuando salga.')
# elif esta_lloviendo == 'no':
#     print('Entonces no voy a usar paraguas cuando salga.')
# else:
#     print('No entiendo que me queres decir con eso.')

# print('mi programa termino')

# primer_numero = 30
# if primer_numero < 20:
#     print('es menor a 20')
# elif primer_numero < 30:
#     print('es menor a 30')
# elif primer_numero < 40:
#     print('es menor a 40')
# elif primer_numero < 50:
#     print('es menor a 50')
    
# if primer_numero < 50:
#     print('es menor a 50')
#     if primer_numero < 40:
#         print('es menor a 40')
#         if primer_numero < 30:
#             print('es menor a 30')
#             if primer_numero < 20:
#                 print('es menor a 20')

# esta_lloviendo = input('Esta lloviendo?? (si/no): ')
#v1
# pepito = ''

# if esta_lloviendo == 'si':
#     pepito = 'soy pepito'
# else:
#     pepito = 'no soy pepito :('

#v2 in-line
# pepito = 'soy pepito' if esta_lloviendo == 'si' else 'no soy pepito :('


#v3 in-line
# pepito = 'soy pepito' if esta_lloviendo == 'si' else 'no soy pepito :(' if esta_lloviendo == 'no' else 'soy ricardo'

# print(pepito)


#Actividad marvel vs capcom

'Grupo A'
'Grupo B'
preferencia = input('Ingrese su preferencia: (Marvel/Capcom) ').capitalize()
nombre = input('Ingrese su nombre: ').upper()

if preferencia == 'Marvel' and nombre < 'M' or preferencia == 'capcom' and nombre > 'N': 
    print('Tu Grupo es el A')
else:
    print('Tu Grupo es el B')