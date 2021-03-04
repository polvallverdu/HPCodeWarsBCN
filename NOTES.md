# Apunts Python 3

## Tipus de variables

Hi ha diferents tipus de variables en python:

```python
# String: text
str("Això es un string")

# Integer: nombre enter
int(69)

# Float: nombre amb decimals
float(69.5)
```
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

També es poden fer llistes

```python

# Les llistes es creen posan elements dintre de [] separant per , queca element

llista_str = ['patates', 'tomaquet']
llista_int = [0, 1]
llista_float = [0.23, 1.45]

#Les llistes començen a contar desde 0 es a dir a la llista de str les patates serien l'elemnet 0
#Per seleccionar un elemnt a una llista hem de posar el nom de la llista més la seva posició

llista_str[0] #això és igual a patata

#per saber el numero de elements que té una llista s'utilitzala funció len()

len(llista_str) # aixó seria 2 perque hi han dos elements
```