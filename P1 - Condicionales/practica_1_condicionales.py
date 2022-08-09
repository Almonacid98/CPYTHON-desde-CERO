#Capitulo 3 : Booleanos, condicionales y entrada de usuario

# Entrada de datos del usuario. Identidicacion de tipo de datos

edad = input("Escribe tu edad: ")
tipo_de_datos = type(edad)
print(edad)
print(tipo_de_datos)


#Booleanos, IF

verdadero = False
falso = True
if(verdadero == True):
    print("Soy verdadero")

if(falso == True):
    print("Son iguales")

if(verdadero == False):
    print("Si soy verdadero falso")


# Operadores de comparacion, elif, else

edad = input("Dime tu edad, por favor: ")
edad = int(edad)
if(edad >= 18):
    print("Eres mayor de edad, puedes pasar")
elif(edad < 0):
    print("Oye, esto no es posible")
elif(edad < 14):
    print("Eres muy pequeño")
else:
    print("Eres menor de edad, no puedes pasar")


# Operadores lógicos and, or, not

edad = input("Dime tu edad, por favor: ")
edad = int(edad)

if(type(edad) == int):
    if(edad > 120 or  edad < 0):
        print("Esto no es posible")
    elif(edad >= 18 and edad < 48):
        print("Puedes entrar a mi club")
    elif(edad < 18 and edad > 15):
        print("Todavia eres muy joven, no puedes entrar")
    else:
        print("No sucedio ninguna de las condiciones")
else:
    print("El tipo de datos no es un numero entero EDAD")

if(not(edad <= 18)):
    print("Puedes pasar")


# Ejercicio
#Comprobar si el usuario introduce un numero, si no es un numero
# sino es un numero debemos indicar que debe introducir un numero entero
# si es un numero, debemos comprobar si es o no par y notificarlo al usuario.

# pistas isnumeric, num%2 = 0

# solucion

numero = input("Introduce un numero: ")

if(not(numero.isnumeric())): #comprobar la entrada si es un numero
    print("lo ingresado no es un numero, debe introducir un numero entero")
elif(numero.isnumeric()):
    numero = int(numero)
    if(numero % 2 == 0):
        print("Su numero ingresado es PAR")
    else:
        print("Su numero ingresado es IMPAR")
