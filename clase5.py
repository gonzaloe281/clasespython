# print(3-2)
# print(2+2)
# print(2*2)
# print(3**2)
# print(3/2)
# print(3//2)
# print(3%2)

#Datos Logicos
# False
# True

#todo tipo de dato se puede transformar a datos logicos (booleano)

#casteando
# bool()

#Operadores relacionales





# string1 = 'ricardo como te va? soy pancho'
# palabra2 = 'hola'
# print(string1 == 'hola')
# print(string1 == palabra2)
# print(string1[8] == 'r')
# print(string1[:2] == 'r')
# print(string1[:2] == 'ri')
# print(string1[0] * 2)


# print(1 < 'a') #rompe porque a es 97 en acssi

# print(False * 55)
# print(True * 55)
# print(True + 55)
# print(True + 0.5)
# print(False == 0.5)
# print(False == 0)
# print(False ==[])


# print(bool(-4))
# print(bool(0))
# print(bool(''))
# print(bool('123asd'))
# print(bool([]))
# print(bool([2,3,54,'pepa','ricardo']))

# expresiones = [
#     False == True,
#     10 >= 2*4,
#     33/3 == 11,
#     True > False,
#     True*5 == 2.5*2
# ]
# # print(False == True)
# # print(10 >= 2*4)
# # print(33/3 == 11)
# # print(True > False)
# # print(True*5 == 2.5*2)

# print(expresiones)

#Operadores logicos

# and or not

# # not
# print(True)
# print(not True)
# print(not 5)   #----> print(not bool(5))
# print(not {1,2,3,4,'pepito'}) # ----> print(not bool({1,2,3,4,'pepito'}))
# print(not {})

# # #and
# True and True ---> True
# False and True ---> False
# True and False ---> False
# False and False ---> False
# print(True and True)
# print(5 == 1 and 4 < 3)
# print(5 == 1 and 'asdfq' <= 'a')

# print(True and 4/0) #da eoor porque sigue leyendo la segunda parte y no se divide entre 0
# print(False and 4/0) #ignora la segunda parte porque lee False


# print(5 and {1,2,3,4,'pepito'})

## or
# True and True ---> True
# False and True ---> True
# True and False ---> True
# False and False ---> False
# print(55 == 60 or 1.5 == 1.5)
# print(66 == 60 or 1.5 == 1.5)
# print(55 == 60 or 1.5 == 1.4)

# print(True or 4/0)
# print(False or 4/0)

# print(5 or {1,2,3,4,'pepito'})

# suma = 0
# suma += 1# suma = suma + 1
# print(suma)
# suma -= 2
# print(suma)
# suma *= 3
# print(suma)
# suma /= 6
# print(suma)
# suma %= 6
# print(suma)

# texto = 'pepito'
# texto += ' corre'
# texto += ' solo'
# print(texto)

nombre= input('Ingrese su nombre: ')
edad= int(input('Ingrese su edad: '))
# 5<edad and edad <20
resultado= nombre != '****' and 5 < edad < 20 and 4 <= len(nombre) <8 and 3*edad > 35
print(resultado)