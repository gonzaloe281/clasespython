# def nombre_de_funcion(parametro):
#     ...
    
# nombre_de_funcion('argumento')

#========================
#========================


# class NombreDeClase:
#     ...
    
# NombreDeClase() 


# nombre_de_clase1 = NombreDeClase() # -> crea un objeto de NombreDeClase

# print(nombre_de_clase1)
# print(type(nombre_de_clase1))
# print(type(1))


#========================
#========================


# class Auto:
#     pass # o ...para no romper por no tener datos adentro
    
# auto1 = Auto()  # <__main__.Auto object at 0x000001DE6F405DF0>
# auto2 = Auto()  # <__main__.Auto object at 0x000001DE6F405D60>

# print(auto1)
# print(auto2)

#========================
#========================
def asd():
    ...

class Auto: #clase
    
    def tocar_bocina(self):  #metodo, va self por convencion
        print('PIIIIIIIIIIIIIIIIIIIIIIIPIIIIIIIIIIIII', self)
        #return

    def avanzar(self, metros_avanzar):  #metodo, va self por convencion
        print('El auto', self, 'avanzo', metros_avanzar, 'metros')

auto1 = Auto()
auto2 = Auto()

print(auto1)
print(auto2)
auto1.tocar_bocina()
auto2.tocar_bocina()
auto1.avanzar(150)
auto2.avanzar(50)
