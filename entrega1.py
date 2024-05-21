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

#------------------------------------


# diccionario para almacenar usuarios y contraseñas
usuarios_contraseñas = {}

# funcion para registrar un nuevo usuario con contraseña (almacenar informacion)
def registrar_usuario():
    usuario = input('Ingrese el nombre de usuario: ').lower()
    contraseña = input('Ingrese la contraseña: ')
    
    if usuario not in usuarios_contraseñas:
        usuarios_contraseñas[usuario] = contraseña
        print(f'Usuario {usuario} registrado exitosamente')
    else:
        print(f'El usuario {usuario} ya existe, por favor elige otro.')

# funcion para verificar la contraseña de un usuario (verificar informacion)
def log_in():
    usuario = input('Ingrese el nombre de usuario: ').lower()
    contraseña = input('Ingrese la contraseña: ')
    
    if usuario in usuarios_contraseñas and usuarios_contraseñas[usuario] == contraseña:
        print(f'Usuario existente y contraseña correcta, Bienvenido {usuario} que gusto verte iniciar sesion.')
    else:
        print('Usuario o contraseña incorrectos. Por favor, intentalo de nuevo.')

# ejecutar codigo
logueo = True
while logueo:
    print('''
          1. Registrar nuevo usuario
          2. Iniciar Sesion
          3. Salir
          ''')
    
    opcion = input('Seleccione una opcion: ')
    
    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        log_in()
    elif opcion == '3':
        print('¡Hasta luego!')
        break
    elif opcion == '4': # funcion para mostrar datos almacenados
        print('''
              Entraste al menu secreto de pruebas,
              te mostrare los usuarios y contraseñas 
              almacenados:
              ''')
        for usuario, contraseña in usuarios_contraseñas.items():
            print(f'Usuario: {usuario} | Contraseña: {contraseña}')
        
    else:
        print('Opcion invalida, seleccione 1, 2 o 3.')