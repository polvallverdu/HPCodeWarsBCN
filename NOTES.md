# Apunts Python 3

## Que son els "#"
S'anomenen comentaris. Tot el que esta darrera d'un "#" no afectará al codi.

## Tipus de variables

Hi ha diferents tipus de variables en python:

```python
# String: text. Sempre van entre '' o ""
str("Això es un string")

# Integer: nombre enter
int(69)

# Float: nombre amb decimals
float(69.5)

# Bool: Cert o fals
bool(true)
bool(false)
```

Per declarar una variable s'ha de fer:

```python
nom_de_la_variable = int(5)
```

**IMPORTANT:** Aquestes variables no poden contindre espais (` `)

### Manipular variables

Els Strings es poden sumar entre si:

```python
a = "Hola "
b = "que tal"

a + b # = "Hola que tal"
```

Els ints i els floats tenen diferents modificadors:

```python
# + = Sumar
5 + 5
# - = Restar
5 - 5
# * = Multiplicar
5 * 5
# / = Dividir (sempre retorna un float)
5 / 5
# // = Dividir (retorna un int)
5 // 5
# % = Modul (residu d'una divisió)
5 % 5
# ** = Potencia (elevar un numero)
5 ** 5 # = 25
```

## Condicionals

També a python es solen utilitzar condicionals(if, else, elif) per posar condicions en la execució de codi

```python

a == b: #aixó es si a és igual a b
a != b: #aixó es si a és derent a b
a > b: #aixó es si a és més gran que b
a < b: #aixó es si a es més petit que b
a => b: #aixó es si a es igual o més gran que b
a =< b: #aixó es si a es igual o més petit que b

a = 2
b = 2

# el condicional if es podria traduir a si es compleix la condició que posis llavorens fa el codi de dintre.

if a == b:
    print('a és igual a b')

# el condicional else és el contrari de if es a dir si no cumpleix la condició del if llavors farà aquesta

if a != b:
    print('a és diferent a b')
else:
    print('a és igual a b')

# el condicional elif és per cuan hi ha més d'una condició es a dir si no es compleix la condició de if anirá a la condició de elif y si tampoc es compleix anirà a un altre elif(si hi ha) sino anirà al else

if a > b:
    print('a és més gran que b')
elif a == b:
    print('a és igual a b')
else:
    print('a és més petita que b')
```

### Keywords

Hi ha diferents paraules que faciliten els condicionals:

```python
if x and y: # S'han de cumplir les dues condicions

if x or y: # S'ha de cumplir una de les dues condicions

if "b" in "abcd": # serà cert quan la primera variable estigui dintre de la segona. També funciona amb llistes.
```

## Lists o Arrays

També es poden fer llistes

```python

# Les llistes es creen posan elements dintre de [] separant per una "," cada element

llista_str = ['patates', 'tomaquet']
llista_int = [0, 1]
llista_float = [0.23, 1.45]

#Les llistes començen a contar desde 0 es a dir a la llista de str les patates serien l'elemnet 0
#Per seleccionar un elemnt a una llista hem de posar el nom de la llista més la seva posició

llista_str[0] #això és igual a patata

#per saber el numero de elements que té una llista s'utilitzala funció len()


len(llista_str) # aixó seria 2 perque hi han dos elements
llista_str.append("aa") # Afegeix "aa" a la llista
llista_str.remove("aa") # Elimina "aa" de la llista
llista_str.reverse() # Inverteix la llista
del llista_str[0] # Elimina l'element que estigui en la posició 0
```

## Diccionaris

Es com una llista, pero té un valor per accedir a un altre valor

```python

diccionari = {"test1": "hola", "test2": "adeu"}

diccionari["test1"] # Això es igual a "hola", perquè "test1" es la seva key.
diccionari["test3"] = "que tal" # Això afegeix al diccionari un element "que tal" amd la key "test3"
```

## Funcions Utils
```python

input() # Demana un input a l'usuari. Sempre torna un string. Per pasaro a int o float s'ha de fer int(input()) o float(input())
print("string") # Imprimeix un string

max(2, 4) # Màxim valor
min(3, 4) # Mínim valor
abs(-69) # Valor absolut
sorted([llista o string]) # Ordena la llista o string alfabeticament
```

## Truquitos 🤙

### Formatejar string

Hi ha dues formes de formatejar strings:

```python
# Forma 1 -> una "f" davant el string, i posar les variables dintre de {}. No funciona si has d'accedir a una llista, o un diccionari (utilitzar []).
print(f"{variable1} {45+2}")

# Amb aquesta forma pots declarar un nombre fix de decimals, o de numeros
var = 5.123456789
var2 = 25
print(f"{var:.2f} {var2:05}") # = 5.12 00025

############   EXTRA   ############

# zeros padding
print(f'{mm}:{ss:02}:{ms:03}')  # 5:03:002

# space padding
print(f'{mm}:{ss:02}:{ms:3}')  # 5:03:  2

# zeros padding and decimals : total 6 len, including dot and 2 decimals
print(f'{mm}:{ss:02}:{ms:06.2f}')  # 5:03:002.00

# zeros leading
print(f'{mm}:{ss:02}:{ms:<03}')  # 5:03:200
```

```python
# Forma 2 -> posar {} en el string, i cridar la funció format() amb les variables dintre de (). Funciona amb llistes i diccionaris.
print("{} gfsdfsdfds {}".format(diccionari["test"], llista[0]))
```
