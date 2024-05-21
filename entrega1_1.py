registros= {}

#funcion para registrar usuarios

def registrar_usuarios():
    usuario= input('Ingrese un nuevo usuario: ').lower()
    password= input('Ingrese una nueva contraseña: ')
    
    if usuario not in registros:
        registros[usuario] = password
        print(f'El usuario {usuario} se ha registrado con exito.')
    else:
        print(f'El  usuario {usuario} ya existe, elegite otro.')
        
# funcion de logeo

def login():
        usuario= input('Ingrese su usuario: ').lower()
        password= input('Ingrese su contraseña: ')
        
        if usuario in registros and registros[usuario] == password:
            print(f'Bienvenido {usuario}, has iniciado sesion.')
        else:
            print('Usuario o contraseña incorrecta, intentalo de nuevo.')

# funcion leer datos
def leer_datos():
    
    for usuario, password in registros.items():
        print(f'''
Nombre:{usuario}
contraseña: {password}
--------------------------
          ''')

# menu
logueo = True
while logueo:
    print('''
          Bienvenido.
          
          1.Registrar Usuario.
          2.Iniciar Sesion.
          3.Ver Registros.
          4.Salir.
          ''')
    
    opcion= input('Seleccione su Opcion: ')
    
    if opcion == '1':
        registrar_usuarios()
    elif opcion == '2':
        login()
    elif opcion == '3':
        leer_datos()
    elif opcion == '4':
        print('''
              Esta seguro?
              1.Si
              2.No
              ''')
        salida= input('Seleccione su opcion:')
        if salida == '1':
            print('Hasta luego.')
            break
        elif salida == '2':
            pass
        else:
            print('Opcion invalida intente de nuevo con 1 o 2.')
    else:
        print('Opcion invalida intente de nuevo con 1,2,3 o 4.')