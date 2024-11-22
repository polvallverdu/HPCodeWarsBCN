# Apuntes Python 3

## Qué son los "#"
Se llaman comentarios. Todo lo que está detrás de un "#" no afectará al código.

## Tipos de variables

Hay diferentes tipos de variables en Python:

```python
# String: texto. Siempre van entre '' o ""
str("Esto es un string")

# Integer: número entero
int(69)

# Float: número con decimales
float(69.5)

# Bool: Verdadero o falso
bool(true)
bool(false)
```

Para declarar una variable se hace:

```python
nombre_de_la_variable = int(5)
```

**IMPORTANTE:** Estas variables no pueden contener espacios (` `)

### Manipular variables

Los Strings se pueden sumar entre sí:

```python
a = "Hola "
b = "qué tal"

a + b # = "Hola qué tal"
```

Los ints y los floats tienen diferentes modificadores:

```python
# + = Sumar
5 + 5
# - = Restar
5 - 5
# * = Multiplicar
5 * 5
# / = Dividir (siempre devuelve un float)
5 / 5
# // = Dividir (devuelve un int)
5 // 5
# % = Módulo (residuo de una división)
5 % 5
# ** = Potencia (elevar un número)
5 ** 5 # = 25
```

## Condicionales

También en Python se suelen utilizar condicionales (if, else, elif) para poner condiciones en la ejecución de código

```python

a == b: #esto es si a es igual a b
a != b: #esto es si a es diferente a b
a > b: #esto es si a es más grande que b
a < b: #esto es si a es más pequeño que b
a => b: #esto es si a es igual o más grande que b
a =< b: #esto es si a es igual o más pequeño que b

a = 2
b = 2

# el condicional if se podría traducir a si se cumple la condición que pongas entonces hace el código de dentro.

if a == b:
    print('a es igual a b')

# el condicional else es lo contrario de if, es decir, si no cumple la condición de if entonces hará esta

if a != b:
    print('a es diferente a b')
else:
    print('a es igual a b')

# el condicional elif es para cuando hay más de una condición, es decir, si no se cumple la condición de if irá a la condición de elif y si tampoco se cumple irá a otro elif (si hay) sino irá al else

if a > b:
    print('a es más grande que b')
elif a == b:
    print('a es igual a b')
else:
    print('a es más pequeña que b')
```

### Palabras clave

Hay diferentes palabras que facilitan los condicionales:

```python
if x and y: # Se deben cumplir las dos condiciones

if x or y: # Se debe cumplir una de las dos condiciones

if "b" in "abcd": # será cierto cuando la primera variable esté dentro de la segunda. También funciona con listas.
```

## Listas o Arrays

También se pueden hacer listas

```python

# Las listas se crean poniendo elementos dentro de [] separando por una "," cada elemento

lista_str = ['patatas', 'tomate']
lista_int = [0, 1]
lista_float = [0.23, 1.45]

#Las listas comienzan a contar desde 0, es decir en la lista de str las patatas serían el elemento 0
#Para seleccionar un elemento en una lista hay que poner el nombre de la lista más su posición

lista_str[0] #esto es igual a patata

#para saber el número de elementos que tiene una lista se utiliza la función len()


len(lista_str) # esto sería 2 porque hay dos elementos
lista_str.append("aa") # Añade "aa" a la lista
lista_str.remove("aa") # Elimina "aa" de la lista
lista_str.reverse() # Invierte la lista
del lista_str[0] # Elimina el elemento que esté en la posición 0
```

## Diccionarios

Es como una lista, pero tiene un valor para acceder a otro valor

```python

diccionario = {"test1": "hola", "test2": "adiós"}

diccionario["test1"] # Esto es igual a "hola", porque "test1" es su key.
diccionario["test3"] = "qué tal" # Esto añade al diccionario un elemento "qué tal" con la key "test3"
```

## Funciones Útiles
```python

input() # Pide un input al usuario. Siempre devuelve un string. Para pasarlo a int o float hay que hacer int(input()) o float(input())
print("string") # Imprime un string

max(2, 4) # Valor máximo
min(3, 4) # Valor mínimo
abs(-69) # Valor absoluto
sorted([lista o string]) # Ordena la lista o string alfabéticamente
```

## Truquillos 🤙

### Formatear string

Hay dos formas de formatear strings:

```python
# Forma 1 -> una "f" delante del string, y poner las variables dentro de {}. No funciona si hay que acceder a una lista o un diccionario (utilizar []).
print(f"{variable1} {45+2}")

# Con esta forma puedes declarar un número fijo de decimales o de números
var = 5.123456789
var2 = 25
print(f"{var:.2f} {var2:05}") # = 5.12 00025

############   EXTRA   ############

# ceros de relleno
print(f'{mm}:{ss:02}:{ms:03}')  # 5:03:002

# relleno de espacios
print(f'{mm}:{ss:02}:{ms:3}')  # 5:03:  2

# ceros de relleno y decimales: total 6 caracteres, incluyendo punto y 2 decimales
print(f'{mm}:{ss:02}:{ms:06.2f}')  # 5:03:002.00

# ceros a la izquierda
print(f'{mm}:{ss:02}:{ms:<03}')  # 5:03:200
```

```python
# Forma 2 -> poner {} en el string, y llamar a la función format() con las variables dentro de (). Funciona con listas y diccionarios.
print("{} gfsdfsdfds {}".format(diccionario["test"], lista[0]))
```

### Girar un String

Cómo invertir un string: 

```python
a = "Hola"[::-1] # -> a será "aloH"
```
