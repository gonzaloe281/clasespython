
# class Auto: #clase
    
#     def __init__(self, marca, modelo, color='blanco'):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         print(f'Se creo el auto {self}')
    
#     def tocar_bocina(self):  #metodo, va self por convencion
#         print('PIIIIIIIIIIIIIIIIIIIIIIIPIIIIIIIIIIIII', self)
#         #return

#     def avanzar(self, metros_avanzar):  #metodo, va self por convencion
#         print('El auto', self, 'avanzo', metros_avanzar, 'metros')

#     # def guardar_fecha_fabricacion(self, fecha_fabricacion): #no es recomendable este metodo
#     #     self.fecha_fabricacion = fecha_fabricacion
        
# auto1 = Auto('Ford','Ka', 'Rojo')
# auto2 = Auto('Fiat', 'Uno', 'Verde')
# auto3 = Auto('Renault', '18')


# print('Este es el auto 1', auto1)
# print(auto1.marca, auto1.modelo, auto1.color)


# print('Este es el auto 2', auto2)
# print(auto2.marca, auto2.modelo, auto2.color)


# print('Este es el auto 3', auto3)
# print(auto3.marca, auto3.modelo, auto3.color)

# # auto1.guardar_fecha_fabricacion('2024-05-07')
# # print(auto1.fecha_fabricacion)

# ------------------------------

# class Auto: #clase
    
#     cantidad_ruedas = 4
    
#     def __init__(self, marca, modelo, color='blanco'):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         # self.cantidad_ruedas = 4
#         print(f'Se creo el auto {self}')
    
#     def tocar_bocina(self):  #metodo, va self por convencion
#         print('PIIIIIIIIIIIIIIIIIIIIIIIPIIIIIIIIIIIII', self)
#         #return

#     def avanzar(self, metros_avanzar):  #metodo, va self por convencion
#         print('El auto', self, 'avanzo', metros_avanzar, 'metros')

# auto1 = Auto('Ford','Ka', 'Rojo')
# auto2 = Auto('Fiat', 'Uno', 'Verde')
# auto3 = Auto('Renault', '18')

# # Auto.cantidad_ruedas = 5
# print(auto1.cantidad_ruedas)
# # # auto2.cantidad_ruedas = 5
# print(auto2.cantidad_ruedas)
# print(auto3.cantidad_ruedas)

# # print(Auto.cantidad_ruedas)

# ------------------------------

# v1
# class Motor:
    
#     def __init__(self, cant_cilindros=6):
#         self.cant_cilindros = cant_cilindros


# class Auto: #clase
    
#     cantidad_ruedas = 4
    
#     def __init__(self, marca, modelo, color='blanco', cant_cilindros =6):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         self.motor = Motor(cant_cilindros)
#         print(f'Se creo el auto {self}')
    
#     def tocar_bocina(self):  #metodo, va self por convencion
#         print('PIIIIIIIIIIIIIIIIIIIIIIIPIIIIIIIIIIIII', self)
#         #return

#     def avanzar(self, metros_avanzar):  #metodo, va self por convencion
#         print('El auto', self, 'avanzo', metros_avanzar, 'metros')

# auto1 = Auto('Ford','Ka', 'Rojo', 12)

# print(auto1.motor)
# print(auto1.motor.cant_cilindros)


# # v2
# class Motor:
    
#     def __init__(self, n_serie, cant_cilindros=6):
#         self.n_serie = n_serie
#         self.cant_cilindros = cant_cilindros


# class Auto: #clase
    
#     cantidad_ruedas = 4
    
#     def __init__(self, marca, modelo, color='blanco', **kwargs):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         self.motor = Motor(**kwargs) # --> Motor(n_serie=123456, cant_cilindros=12)
#         print(f'Se creo el auto {self}')
    
#     def tocar_bocina(self):  #metodo, va self por convencion
#         print('PIIIIIIIIIIIIIIIIIIIIIIIPIIIIIIIIIIIII', self)
#         #return

#     def avanzar(self, metros_avanzar):  #metodo, va self por convencion
#         print('El auto', self, 'avanzo', metros_avanzar, 'metros')

# auto1 = Auto('Ford','Ka', 'Rojo', n_serie=123456, cant_cilindros = 12)

# print(auto1.motor)
# print(auto1.motor.n_serie)
# print(auto1.motor.cant_cilindros)

# ------------------------


# v2
class Motor:
    
    def __init__(self, numero_serie, cant_cilindros=6):
        self.numero_serie = numero_serie
        self.cant_cilindros = cant_cilindros


class Auto: #clase
    
    cantidad_ruedas = 4
    
    def __init__(self, marca, modelo, color='blanco', **datos_motor): #__init__ para la creacion de un objeto
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.motor = Motor(**datos_motor) # --> Motor(n_serie=123456, cant_cilindros=12)
        print(f'Se creo el auto {self}')
    
    def __str__(self):   # --> transforma el objeto a string
        return f'Auto {self.marca} {self.modelo} de color {self.color}'
    
    def tocar_bocina(self):  #metodo, va self por convencion
        print('PIIIIIIIIIIIIIIIIIIIIIIIPIIIIIIIIIIIII', self)
        #return

    def avanzar(self, metros_avanzar):  #metodo, va self por convencion
        print('El auto', self, 'avanzo', metros_avanzar, 'metros')

auto1 = Auto('Ford','Ka', 'Rojo', numero_serie=123456, cant_cilindros = 12)

print(auto1) # --> print(str(auto1))


#===========================
#===========================


class Consecionaria:
    
    def __init__(self, concesionaria):
        self.concesionaria = concesionaria
        self.autos = []
        
    def __str__(self):
        return f'Listado de autos en la concesionaria "{self.concesionaria}"'
    
    def __len__(self):
        return len(self.autos)
    
    def agregar_auto(self, auto):
        if auto and auto.color.capitalize() == 'Negro':
            self.autos.append(auto)
        else:
            print('Te flato el auto de color negro.')
            
    def __getitem__(self, posicion):
        try:
            return self.autos[posicion]
        except:
            return 'No se encontro ese auto'
        
    def __setitem__(self, posicion, nuevo_auto):
        try:
            if nuevo_auto.color == 'Negro':
                self.autos[posicion] = nuevo_auto
            else:
                print('El auto no es negro.')
        except:
            print('No se pudo modificar el auto de la posicion {posicion}.')
            
    def __iter__(self):
        for auto in self.autos:
            yield auto # <--- queda en stand by, en espera
            
consecionaria = Consecionaria('Pepito')

print(consecionaria)
print(len(consecionaria))
auto1.color = 'negro'
# consecionaria.agregar_auto(auto1)
print(consecionaria.autos)
consecionaria[0] = auto1