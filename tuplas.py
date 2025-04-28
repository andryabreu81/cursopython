# ejemplos y ejercicios de tuplas
# Definicion de tuplas
# es una coleccion de elementos inmutables ordenados
# se definen con parentesis ()
# se pueden almacenar diferentes tipos de datos
# se pueden almacenar listas dentro de tuplas
# se pueden almacenar tuplas dentro de listas
# se pueden almacenar tuplas dentro de tuplas


tupla = ('naranjas','manzanas','peras','kiwis','mangos')
print(tupla)# imprime la tupla
print(type(tupla))# imprime el tipo de dato
print(len(tupla))# imprime la longitud de la tupla
print(tupla[0])# imprime el primer elemento de la tupla
print(tupla[0:2])# imprime parte de la tupla


# como cambiar los datos de una tupla
vehiculos = ('carro','moto','avion','barco','yate','ferri','camion')
print(vehiculos)# imprime la tupla

print(len(vehiculos))# imprime la longitud de la tupla

# tuplas con varios tipos de datos
tupla = ('naranjas', 1, 2.5, True, [1,2,3], (1,2,3))
print(tupla)# imprime la tupla
print(type(tupla))# imprime el tipo de dato
# tuplas con listas
tupla = ('naranjas', [1,2,3], (1,2,3))
print(tupla)# imprime la tupla
# tuplas con tuplas
tupla = ('naranjas', (1,2,3), (1,2,3))
print(tupla)# imprime la tupla

# convertir un tupla a lista
tupla = ('naranjas', 'manzanas', 'peras', 'kiwis', 'mangos')
lista = list(tupla)
print(lista)# imprime la lista
# convertir una lista a tupla
lista = ['naranjas', 'manzanas', 'peras', 'kiwis', 'mangos']
tupla = tuple(lista)
print(tupla)# imprime la tupla

# para agregar un elemento a una tupla, primero se convierte a lista

lista.append('moras')
print(lista)# imprime la tupla

# desempaquetamiento de tuplas
vehiculos = ('bicicleta','moto','avion','barco','yate','ferri','camion')
(a,b,c,d,e,f,g) = vehiculos
print(a)# imprime la tupla

(*dosruedas,avion,barco,yate,ferri,camion) = vehiculos
print(dosruedas)# imprime la tupla

# recorrido de tuplas
for vehiculo in vehiculos:
    print(vehiculo)# imprime la tupla
# recorrido de tuplas con un for y un range
print('recorrido de la tupla con un for y un range')
for i in range(len(vehiculos)):
    print(vehiculos[i])# imprime la tupla
# recorrido de tuplas con un for y un range
print('recorrido de la tupla con un for y un range')
for i in range(len(vehiculos)):
    print(f"{i+1}. {vehiculos[i]}")# imprime la tupla


# shorthands
[print(vehiculo) for vehiculo in vehiculos]