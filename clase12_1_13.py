# class Motor:
    
#     def __init__(self, numero_serie, cant_cilindros=6):
#         self.numero_serie = numero_serie
#         self.cant_cilindros = cant_cilindros


# class Auto: #clase
    
#     cantidad_ruedas = 4
    
#     def __init__(self, marca, modelo, num_chasis, color='blanco', **datos_motor): #__init__ para la creacion de un objeto
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         self.motor = Motor(**datos_motor) # --> Motor(n_serie=123456, cant_cilindros=12)
#         self.__num_chasis = num_chasis # el __ adelante limita el acceder desde afuera
#         print(f'Se creo el auto {self}')
    
#     def __str__(self):   # --> transforma el objeto a string
#         return f'Auto {self.marca} {self.modelo} de color {self.color}'
    
#     def tocar_bocina(self):  #metodo, va self por convencion
#         print('PIIIIIIIIIIIIIIIIIIIIIIIPIIIIIIIIIIIII', self)
#         #return

#     def avanzar(self, metros_avanzar):  #metodo, va self por convencion
#         print('El auto', self, 'avanzo', metros_avanzar, 'metros')

    
    
#     def mostrar_num_chasis(self): # getter, acceder de manera interna al dato
#         if self.color == 'Blanco':
#             print(f'El numero de chasis para {self} es {self.__num_chasis}')
        
#         else:
#             print('No te lo puedo mostrar porque soy un auto blanco.')
            
#     def actualizar_num_chasis(self, nuevo_num_chasis): # setter
#         if self.color != 'Blanco':
#             self.__num_chasis = nuevo_num_chasis
#         else:
#             print('No puedo modificar mi numero de chasis porque soy un auto blanco')
    
    
# auto1 = Auto('Ford','Ka', 132456, 'Blanco', numero_serie=123456, cant_cilindros = 12)
# # print(auto1.__num_chasis) #rompe porque esta pseudo privado
# # print(auto1._Auto__num_chasis) #aca se ve pero no se usa
# auto1.mostrar_num_chasis()
# auto1.actualizar_num_chasis(555)

#===========================================================================
#===========================================================================

# class Vehiculo: #clase padre
    
#     def __init__(self, marca, color): #__init__ para la creacion de un objeto
#         self.marca = marca
#         self.color = color
#         print(f'Se creo {self}')
    
#     def __str__(self):   # --> transforma el objeto a string
#         return f'{type(self).__name__} {self.marca} de color {self.color}'
    
    
#     def tocar_bocina(self):  #metodo, va self por convencion
#         print('PIIIIIIIIIIIIIIIIIIIIIIIPIIIIIIIIIIIII')
    


# class Auto(Vehiculo): #clase Heredada
#     ...    
#     # def __str__(self):   # --> transforma el objeto a string
#     #     return f'este es el str del auto'
    
        
# class Moto(Vehiculo):
#     ...    
#     # def __str__(self):   # --> transforma el objeto a string
#     #     return f'este el str de la moto'

# class Lancha(Vehiculo):
#     ...
    
# vehiculo = Vehiculo('Ford', 'verde')
# vehiculo.tocar_bocina()
# print(vehiculo)


# auto = Auto('Fiat', 'blanco')
# auto.tocar_bocina()
# print(auto)


# moto = Moto('BMW', 'negra')
# moto.tocar_bocina()
# print(moto)


# lancha = Lancha('Lamborghini', 'blanca')
# lancha.tocar_bocina()
# print(lancha)

# # autito = auto
# # print(autito)

#===========================================================================
#===========================================================================

# class Vehiculo: #clase padre
    
#     def __init__(self, marca, color): #__init__ para la creacion de un objeto
#         self.marca = marca
#         self.color = color
#         print(f'Se creo {self}')
    
#     def __str__(self):   # --> transforma el objeto a string
#         return f'{type(self).__name__} {self.marca} de color {self.color}'
    
    
#     def tocar_bocina(self):  #metodo, va self por convencion
#         print('PIIIIIIIIIIIIIIIIIIIIIIIPIIIIIIIIIIIII')
    


# class Auto(Vehiculo): #clase Heredada
#     def tocar_bocina(self):
#         print('Soy el auto tocando bocina!')
    
        
# class Moto(Vehiculo):
#     ...    
#     # def __str__(self):   # --> transforma el objeto a string
#     #     return f'este el str de la moto'

# class Lancha(Vehiculo):
#     ...
    
# vehiculo = Vehiculo('Ford', 'verde')
# vehiculo.tocar_bocina()
# print(vehiculo)


# auto = Auto('Fiat', 'blanco')
# auto.tocar_bocina()
# print(auto)


# moto = Moto('BMW', 'negra')
# moto.tocar_bocina()
# print(moto)


# lancha = Lancha('Lamborghini', 'blanca')
# lancha.tocar_bocina()
# print(lancha)

# # autito = auto
# # print(autito)

#===========================================================================
#===========================================================================

# class Vehiculo: #clase padre
    
#     def __init__(self, marca, color): #__init__ para la creacion de un objeto
#         self.marca = marca
#         self.color = color
#         print(f'Se creo {self}')
    
#     def __str__(self):   # --> transforma el objeto a string
#         return f'{type(self).__name__} {self.marca} de color {self.color}'
    
    
#     def tocar_bocina(self):  #metodo, va self por convencion
#         print('PIIIIIIIIIIIIIIIIIIIIIIIPIIIIIIIIIIIII')
    
#     def metodo_solo_vehiculo(self):
#         print('Metodo solo vehiculo!!!')
    

# class Auto(Vehiculo): #clase Heredada
#     #v1
#     # def __init__(self, marca, color, cant_ruedas): #__init__ para la creacion de un objeto
#     #     self.marca = marca
#     #     self.color = color
#     #     self.cant_ruedas = cant_ruedas
#     #     print(f'Se creo {self}')
    
#     # v2
#     def __init__(self, marca, color, cant_ruedas):
#         self.cant_ruedas = cant_ruedas
#         super().__init__(marca, color)
    
#     #v3
#     # def __init__(self, cant_ruedas, **kwargs):
#     #     self.cant_ruedas = cant_ruedas
#     #     super().__init__(**kwargs)
    
#     def tocar_bocina(self):
#         super().tocar_bocina()
#         print('Soy el auto tocando bocina')
#         super().tocar_bocina()

#     def metodo_solo_auto(self):
#         super().metodo_solo_vehiculo()
#         print('Soy el auto tocando bocina')
#         super().tocar_bocina()
    
# vehiculo = Vehiculo('Ford', 'verde')
# vehiculo.tocar_bocina()
# print(vehiculo)

# # v2
# auto = Auto('Fiat', 'blanco', 4)

# # v3
# # auto = Auto(marca='Fiat', color='blanco', cant_ruedas=4)
# auto.tocar_bocina()
# print(auto.cant_ruedas)
# auto.metodo_solo_auto()


# #===========================================================================
# #===========================================================================


# class Vehiculo: #clase padre
    
#     def __init__(self, marca, color): #__init__ para la creacion de un objeto
#         self.marca = marca
#         self.color = color
#         print(f'Se creo {self}')
    
#     def __str__(self):   # --> transforma el objeto a string
#         return f'{type(self).__name__} {self.marca} de color {self.color}'
    
    
#     def tocar_bocina(self):  #metodo, va self por convencion
#         print('PIIIIIIIIIIIIIIIIIIIIIIIPIIIIIIIIIIIII')
    
#     def metodo_solo_vehiculo(self):
#         print('Metodo solo vehiculo!!!')

# class VehiculosConRuedas(Vehiculo):

#     def __init__(self, marca, color, cant_ruedas):
#         self.cant_ruedas = cant_ruedas
#         super().__init__(marca, color)


# class Auto(VehiculosConRuedas): #clase Heredada
#         ...       
            
# class Moto(VehiculosConRuedas):
#         ...    

# class Lancha(Vehiculo):
#         ...

# auto = Auto('Fiat', 'blanco', 4)
# moto = Moto('BMW', 'negra', 2)
# lancha = Lancha('Lamborghini', 'blanca')


# print(auto.cant_ruedas)
# print(moto.cant_ruedas)

# auto.tocar_bocina()
# lancha.tocar_bocina()

#===========================================================================
#===========================================================================


class Vehiculo: #clase padre
    
    def __init__(self, marca, color): #__init__ para la creacion de un objeto
        self.marca = marca
        self.color = color
        print(f'Se creo {self}')
    
    def __str__(self):   # --> transforma el objeto a string
        return f'{type(self).__name__} {self.marca} de color {self.color}'
    
    
    def tocar_bocina(self):  #metodo, va self por convencion
        print('PIIIIIIIIIIIIIIIIIIIIIIIPIIIIIIIIIIIII')
    

class Acuatico():
    
    def avanzar(self, millas_a_avanzar):  #metodo, va self por convencion
        print('El ', type(self).__name__, self, 'avanzo', millas_a_avanzar, 'millas')
    
    
class Terrestre():

    def __init__(self, marca, color, cant_ruedas):
        self.cant_ruedas = cant_ruedas
        super().__init__(marca, color)
        
    def avanzar(self, metros_a_avanzar):  #metodo, va self por convencion
        print('El ', type(self).__name__, 'avanzo', metros_a_avanzar, 'metros')

class Auto(Vehiculo, Terrestre): #clase Heredada multiple
    def __init__(self, marca, color, cant_ruedas):
        super().__init__(marca, color)
    
    def tocar_bocina(self):  #metodo, va self por convencion
        print('Toque bocina en mi auto')
    

class Lancha(Vehiculo, Acuatico):
    
    def tocar_bocina(self):  #metodo, va self por convencion
        print(f'Toque bocina en mi {self.marca}')
    

auto = Auto('Fiat', 'blanco', 4)
lancha = Lancha('Lamborghini', 'blanca')

auto.avanzar(15)
lancha.avanzar(156)

print(Auto.__mro__)
print(Vehiculo.__mro__)


lista = [auto, lancha]

for objeto in lista:
    objeto.tocar_bocina()
    