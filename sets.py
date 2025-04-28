# conjuntos o sets, es una coleccion que permite almacenar elementos unicos en una variable
# se definen con llaves {}
# se pueden almacenar diferentes tipos de datos
# aunque hayan elementos duplicados, solo se almacenara uno
# se pueden agregar o elminar elementos, pero no se pueden modificar poreue no tienen un orden
# los conujuntos no permiten duplicados
# los conjuntos no tienen un indice

conjunto = {1, 2, 3, 4, 5}
print(conjunto)  # imprime el conjunto

print('no imprime elementos duplicados')
conjunto2 = {1, 2, 3, 3, 4, 5, 1}
print(conjunto2) # {1, 2, 3, 4, 5}
print(type(conjunto2))  # imprime el tipo de dato
print(len(conjunto2))  # imprime la longitud del conjunto

# constructor de conjuntos
conjunto3 = set(('hola','soy','un','conjunto'))
print(conjunto3)  # imprime el conjunto
print(type(conjunto3))  # imprime el tipo de dato
print(len(conjunto3))  # imprime la longitud del conjunto


# verificas que un elemento este en el conjunto
if 'hola' in conjunto3:
    print('hola esta en el conjunto')
else:
    print('hola no esta en el conjunto')

if 'adios' not in conjunto3:
    print('adios no esta en el conjunto')
else:
    print('adios esta en el conjunto')

# agregar elementos a un conjunto
print('agregar elementos a un conjunto')
conjunto3.add('adios')
print(conjunto3)  # imprime el conjunto
conjunto3.add('hola')  # no se agrega porque ya existe
print(conjunto3)  # imprime el conjunto

# eliminar elementos de un conjunto
print('eliminar elementos de un conjunto')
conjunto3.remove('hola') # da error si no existe
print(conjunto3)  # imprime el conjunto
conjunto3.discard('hola')  # no se elimina porque no existe, no da error
print(conjunto3)  # imprime el conjunto

conjunto3.pop()  # elimina un elemento aleatorio
print(conjunto3)  # imprime el conjunto


# eliminar todos los elementos de un conjunto
print('eliminar todos los elementos de un conjunto')
conjunto3.clear()
print(conjunto3)  # imprime el conjunto
# eliminar un conjunto
print('eliminar un conjunto')
del conjunto3
# print(conjunto3)  # imprime el conjunto

# crear un conjunto vacio
conjunto_vacio = set()
print(conjunto_vacio)  # imprime el conjunto

# union de conjuntos
print('union de conjuntos')
conjunto4 = {1, 2, 3}
conjunto5 = {4, 5, 6}
conjunto6 = conjunto4.union(conjunto5)
print(conjunto6)  # imprime el conjunto
conjunto7 = conjunto4 | conjunto5
print(conjunto7)  # imprime el conjunto

# interseccion de conjuntos
print('interseccion de conjuntos')
conjunto8 = {1, 2, 3}
conjunto9 = {3, 4, 5}
conjunto10 = conjunto8.intersection(conjunto9)
print(conjunto10)  # imprime el conjunto
conjunto11 = conjunto8 & conjunto9
print(conjunto11)  # imprime el conjunto

# diferencia de conjuntos
print('diferencia de conjuntos')
conjunto12 = {1, 2, 3}
conjunto13 = {3, 4, 5}
conjunto14 = conjunto12.difference(conjunto13)
print(conjunto14)  # imprime el conjunto
conjunto15 = conjunto12 - conjunto13
print(conjunto15)  # imprime el conjunto

# update de conjuntos
print('update de conjuntos')
conjunto16 = {1, 2, 3}
conjunto17 = {3, 4, 5}
conjunto16.update(conjunto17)
print(conjunto16)  # imprime el conjunto

# diferencia simetrica de conjuntos
print('diferencia simetrica de conjuntos')
conjunto18 = {1, 2, 3}
conjunto19 = {3, 4, 5}
conjunto20 = conjunto18.symmetric_difference(conjunto19)
print(conjunto20)  # imprime el conjunto
conjunto21 = conjunto18 ^ conjunto19
print(conjunto21)  # imprime el conjunto

# subset de conjuntos
print('subset de conjuntos')
conjunto22 = {1, 2, 3}
conjunto23 = {1, 2, 3, 4, 5}
print(conjunto22.issubset(conjunto23))  # imprime True
print(conjunto23.issubset(conjunto22))  # imprime False

# superset de conjuntos
print('superset de conjuntos')
conjunto24 = {1, 2, 3}
conjunto25 = {1, 2, 3, 4, 5}
print(conjunto24.issuperset(conjunto25))  # imprime False
print(conjunto25.issuperset(conjunto24))  # imprime True

# comparacion de conjuntos
print('comparacion de conjuntos')
conjunto26 = {1, 2, 3}
conjunto27 = {1, 2, 3}
print(conjunto26 == conjunto27)  # imprime True
print(conjunto26 != conjunto27)  # imprime False
conjunto28 = {1, 2, 3}
conjunto29 = {1, 2, 3, 4, 5}
print(conjunto28 == conjunto29)  # imprime False
print(conjunto28 != conjunto29)  # imprime True

# recorridos de conjuntos
print('recorridos de conjuntos')
conjunto30 = {1, 2, 3}
for elemento in conjunto30:
    print(elemento)  # imprime el conjunto





# shorthands
print('shorthands')
[print(elemento) for elemento in conjunto30]