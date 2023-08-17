# Capitulo 4 : Bucles
# Introduccion a listas
"""
numeros = [1, 2, 3, 4, 5]
print(numeros)
print(numeros[0])
print(numeros[2])

print(len(numeros))

texto = ["juan", "Botella", "Taza"]
print(texto)
print(texto[2])

variadas = [1, 2.3, False, "Hola"]
print(variadas)
print(variadas[3])
"""
# Bucles: bucle for
"""
for x in range(5):
    print(x)

for x in range(1, 7):
    print(x)

for x in range(5, 20, 2):
    print(x)
"""
# Mini ejemplo, imprimir solo las vocales de una palabra
"""
palabra = "cocodrilo"
for letra in palabra:
    if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        print(letra)
    else:
        print("Es una consonante")
"""
# Mini ejemplo, iterar sobre una lista
numeros = [22, 33, 44, 55]
"""
for numero in numeros:
    print(numero)
    numero += 10
    print(numero)
print(numeros)
"""
"""
for indice in range(len(numeros)):
    numeros[indice] += 10
print(numeros)
"""
# blucles while
"""
contador = 0
while(contador < 10):
    print(contador)
    contador += 1
"""
"""
letra_encontrada = False
letra = "a"
frase = "En este momento estoy buscando la letra a"

indice = 0
"""
"""
while(not(letra_encontrada)):
    if(frase[indice] == "a"):
        letra_encontrada = True
        print(f"Letra encontrada {letra} en la posicion {indice}")
    else:
        indice += 1

"""
# break, continue, pass
# Break
"""
frase = "En este momento estoy buscando la letra a"

letra = "y"

for caracter in frase:
    if(caracter == letra):
        print(f"Letra {letra} encontrada en la posicion {frase.index(caracter)}")
        print(caracter)
        break
    else:
        print("Letra no encontrada de momento")
     """
# Continue
"""
frase = "Hola Ana"
letra = "a"
contador = 0

for caracter in frase:
    if(caracter == letra):
        contador += 1
        print(f"Letra encontrada {contador} veces")
        continue
    print("No he encontrado nada")
"""
# Pass
"""
lista = [0, 10, 20, 30]
for num in lista:
    if(num == 10):
        pass
    print(f"El valor de numero es: {num}")

def funcion_cutre(arg1, arg2):
    pass
def funcion_dos(arg1, arg2):
    pass
"""
# Else
"""
frase = " Todos los caracteres de una frase "
cont = 0

for caracter in frase:
    cont += 1
    if(caracter == "l"):
        break
else:
    print(f"La frase tiene {cont} caracteres")

"""
#EJERCICIO PRACTICO PARA INTERPRETACION DE LOS TEMAS DADOS
#Ejercicio : El usuario debe adivinar un numero entre 0 y 10
#el programa debera pedir que el usuario introduzca un numero
#y debe decir si ha acertado, si el numero a adivinar es menor
#o mayor que el que ha introducido

numero_correcto = 5

def pedir(numero_adivinar):
    num_usuario = int(input("Debes ingresar un numero a adivinar:"))
    if(num_usuario == numero_adivinar):
        print("El numero introducido es correcto!")
        return True
    elif(num_usuario < numero_adivinar):
        print("El numero es menor, pero estas cerca, introduce un numero mas grande")
        return False
    elif(num_usuario > numero_adivinar):
        print("El numero es mayor, debe ser mas pequeño")
        return False

while(True):
    if(pedir(numero_correcto)):
        print("Fin del juego")
        break