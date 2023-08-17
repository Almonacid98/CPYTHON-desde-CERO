# Capitulo 5: Listas
# Repaso de conceptos básicos

numeros = [1, 2, 3, 4, 5]
print(numeros)
primera_posicion = numeros[0]

longitud = len(numeros)
print(f"El primer valor de la primera posicion es: {primera_posicion}\nla longitud de la lista es: {longitud}")


for num in numeros:
    print(num)

# Apartado 2  : Indexado y sublistas

lista = ["dale", "un", "buen", "like", "crack"]

ultima_posicion = lista[-1]
penultimo_elemento = lista[-2]

print(lista)
print(ultima_posicion)          # indices negativos
print(penultimo_elemento)

sublista = lista[1:4]
print(sublista)
sublista = lista[:4]
print(sublista)
sublista = lista[2:]
print(sublista)

sublista = lista[-4:-1]
print(sublista)


# Apartado 3: Comprobar si una lista contiene o no un elemento
"""
lista = ["dale", "un", "buen", "like", "crack"]
palabra = "like"
palabra_dos = "melocoton"

if(palabra in lista):
    print("La palabra pertenece a la lista")

if(palabra_dos not in lista):
    print("La palabra no esta en la lista")
"""

# Apartado 4: Modificar elementos de una lista
"""
lenguajes = ["C", "Java", "Python", "JavaScript", "kotlin", "Ruby", "rust"]
print(lenguajes)
lenguajes[1] = "Angular"
print(lenguajes)
lenguajes[0] = lenguajes[0] + "++"
print(lenguajes)

lenguajes[2:4] = ["Anaconda", "TypeScript"]
print(lenguajes)

lenguajes[4:5] = ["ñe", "l", "F"]
print(lenguajes)
"""

# Apartado 5: Métodos de las listas = Añadir elementos
# En python podemos utilizar métodos con las listas.
# Para ejecutar estos métodos : variable_de_tipo_lista.metodos.()
"""
lenguajes = ["C", "Java", "Python", "JavaScript", "kotlin", "Ruby", "rust"]
print(lenguajes)
lenguajes.insert(1, "C++")
print(lenguajes)

lenguajes.append("TypeScript")
print(lenguajes)

lenguajes_dos = [ "Angular", "Vue", "React"]
lenguajes.extend(lenguajes_dos)
print(lenguajes)
print(lenguajes_dos)

lenguajes_dos.extend(lenguajes)
print(lenguajes_dos)
"""
# Apartado 6: Métodos de las listas = eliminar elementos

frutas = ["banana", "kiwi", "frutilla", "durazno", "Cereza" ]

print(frutas)
elemento_eliminado = frutas.pop()
print(elemento_eliminado)
print(frutas)

frutas.pop(0)
print(frutas)

frutas.remove("kiwi")
print(frutas)

del frutas[0]
print(frutas)



# Apartado 8: Métodos de las listas = funcion index
"""
indice = frutas.index("durazno")
print(indice)
"""

# Apartado 9: EJERCICIO
# Enunciado: Tenemos un texto donde queremos encontrar palabras clave
# las palabras clave pueden ser hasta 5 y debemos pedirselas al usuario
# y guardarlas en una lista

# Si el usuario quiere poner menos de 5 palabras clave, debera escribir
# "fin" para terminar de introducir datos. Si el usuario introduce
# numeros o nada, debemos eliminarlos de la lista antes de la busqueda

# En otra lista, debemos guardar el numero de veces que aparece cada
# palabra clave en nuestro texto. Por ejemplo : si las palabraas clave son ordenador
# y portátil y aparecen 5 y 7 veces respectivamente, nuestras listas deberan
# ser así:
#           *   keywords = ["ordenador", "portátil"]
#           * ocurrencias = [5, 7]

# Pista: Podemos pasar de una cadena de texto a una lista de palabras mediante
# el método texto.split(). Por ejemplo:

# texto = "Hola que tal"
# print(texto.split())
# texto = ["hola", "que", "tal"]

# SOLUCION:

texto = """"Seguramente hayas notado que tu productividad ha bajado desde que trabajas desde casa. 
Es muy importante que logremos teletrabajar efectivamente y de manera autorregulada. 
Esto se traduce en finalizar antes nuestras tareas y evitar jornadas laborales interminables.
El primer consejo y uno de los más importantes ya te lo he dado en el apartado anterior. 
Tenemos que construir un espacio de trabajo en el que nos sintamos cómodos y dispongamos de todas las herramientas necesarias para teletrabajar. 
En la medida de lo posible, es importante teletrabajar siempre en el mismo lugar. 
De esta forma, nuestro cerebro asocia el sitio con la acción de trabajar y nos hará estar más focalizados en nuestras tareas."""

keywords = []
ocurrencias = []

for palabra_clave in range(5):
    keyword = input("Ingrese la palabras clave, deben ser al menos 5 0 fin para terminar: ")
    if keyword == "fin":
        break
    else:
        keywords.append(keyword)

print(keywords)

posicion = 0
while(True):
    if posicion >= len(keywords):
        break
    if keywords[posicion] == '':
        keywords.pop(posicion)
    elif keywords[posicion].isnumeric():
        keywords.pop(posicion)
    else:
        posicion += 1
print("lista de keywords corregida:")
print(keywords)

texto = texto.replace(".", "").replace(",", "").split()

for x in range(len(keywords)):
    ocurrencias.append(0)

for palabra in texto:
    for keyword in keywords:
        if keyword == palabra:
            pos = keywords.index(keyword)
            ocurrencias[pos] += 1
            break



print(ocurrencias)