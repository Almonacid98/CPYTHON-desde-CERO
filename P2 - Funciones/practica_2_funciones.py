# Cap 2 Practica de Funciones Funciones
# Definicion de las funciones
#Cada función ejecutar por separado o comentar para probarlas
#resuelve una tarea especifica
def saludar():                  #Definir la funcion
    print("¿Hola que tal?")
"""
saludar()      #llamar la funcion
saludar()
saludar()
"""
# Funciones con argumentos

def saludar_dos(nombre):
    print("Hola" + " " + nombre + " " + "¿Que tal?")
"""
saludar_dos("juan")
saludar_dos("Angela")
"""
# Funciones con retorno

def suma(a, b):
    resultado = a + b
    return resultado
"""
valor = suma(10, 5)
print(valor)
valor = suma(22, 1)
print(valor)
"""
def suma_dos(a, b):
    return a + b

"""valor = suma_dos(10, 5)
print(valor)"""

def son_iguales(num1, num2):
    return num1 == num2
"""
verdad = son_iguales(10, 10)
if(verdad):
    print("Son iguales")
else:
    print("Son diferentes")
print(verdad)
verdad = son_iguales(10, 1)
print(verdad)
"""

# Funciones con argumentos con valor por defecto

def saludar_por_defecto(nombre="Estebam"):
    print("Hola" + " " + nombre + " " + "¿Que tal?")

saludar_por_defecto()
saludar_por_defecto("Andrea")


# Funciones que retornan varios valores

def suma_y_resta(a, b):
    suma = a + b
    resta = a - b
    return suma, resta
"""
resultados = suma_y_resta(15, 10)
print(resultados)
"""
def suma_y_resta_2(a, b):
    return a + b, a - b
"""
valores = suma_y_resta_2(10, 10)
print(valores)

resultado1, resultado2 = suma_y_resta_2(10, 10)
print("Los resultados son:\nSuma: "+ str(resultado1) + "\nResta: "+ str(resultado2))
"""

# EJERCICIO1 : Funcion máximo -> Dados dos numeros, la funcion debe encontrar
#cual de las dos es la mas grande y retornarlo. Extra: Se deben comprobar que los
#argumentos de la funcion sean tipo int o float. si alguno de estos dos
# no lo es, mostrar un mensaj de error y retornarlo False.

# SOLUCION

def encontrar_maximos(num1, num2):
    if((type(num1) == int or type(num1) == float) and (type(num2) == int or type(num2) == float)):
        if(num1 == num2):
            print("Los numeros ingresados son iguales")
            return num1
        elif(num1 > num2):
            return num1
        else:
            return num2
    else:
        print("Error los datos introducidos no son del tipo float ni del tipo entero")
        return False
numeros = encontrar_maximos(6, 5)
if(type(numeros) != bool):
    print("El maximo es:" + str(numeros))

numeros = encontrar_maximos(2, "pedro")
if(type(numeros) != bool):
    print("El maximo es:" + str(numeros))


# EJERCICIO 2 : Mini calculadora. Pedir al usuario una operacion y dos numeros
#las operaciones puden ser suma, resta, potencia. Si introduce una operacion diferente
#a estas, mostrar un mensaje de error. Si la operacion es correcta, mostrar el resultado

#SOLUCION
def calculadora():
        operacion = input("¿Que operacion deseea realizar? :")
        num1 = float(input("Numero 1: "))
        num2 = float(input("Numero 2: "))
        if(operacion == "suma"):
            print(num1 + num2)
        elif(operacion == "resta"):
            print(num1 - num2)
        elif(operacion == "potencia"):
            print(num1 ** num2)
        else:
            print("Error: La operacion introducida no se encuantra en la calculadora")

calculadora()

