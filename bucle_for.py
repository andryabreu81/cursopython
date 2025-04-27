# bucles loops con for
from pydoc import text


print('ejemplos de bucles con for')

for i in range(1, 11):
    print(f'i: {i}')

print('2do ejemplo, bucle for con lista')
lista = ['a', 'b', 'c', 'd', 'e','f','g','h']
for letra in lista:
    print(f'letra: {letra}')

print('3er ejemplo, bucle for con lista y range')
for i in range(len(lista)):
    print(f'letra: {lista[i]}')

# imprime cada dos posiciones desde la cero
print('4to ejemplo, bucle for con lista y range')
for i in range(0, len(lista), 2):
    print(f'letra: {lista[i]}')


# imprime la lista al reves
print('5to ejemplo, bucle for con lista y range')
for i in range(len(lista)-1, -1, -1):
    print(f'letra: {lista[i]}')

print('6to ejemplo')
lenguajes = ['PHP','Python','Angular','Java','JavaScript','SQL']

x = 1
for lenguaje in lenguajes:
    print(f'{x}. Lenguaje: {lenguaje}')
    x += 1 # incrementa en 1 a x

print('7to ejemplo, romper bucle en una posicion del arreglo')
lenguajes = ['PHP','Python','Angular','Java','JavaScript','SQL']
 
x = 1
for lenguaje in lenguajes:
    if (x == 3):
        break
    print(f'{x}. Lenguaje: {lenguaje}')
    x += 1 # incrementa en 1 a x

print('8vo ejemplo, romper bucle en una posicion del arreglo, pero continua')
lenguajes = ['PHP','Python','Angular','Java','JavaScript','SQL']

z = 1
for lenguaje in lenguajes:
    if (z == 3):
        continue
    print(f'{z}. Lenguaje: {lenguaje}')
    z += 1 # incrementa en 1 a z


# ejemplo para recorrer un string
print('recorrido de un string')
text = 'esto es un script de pruebas con un for'

# imprime cada letra del string incluyendo espacios vacios
for letra in text:
    print(f'letra: {letra}')

# ejemplo de un for dentro de otro for
letras = ['a', 'b', 'c']
numeros = [1, 2, 3]

# imprime todos lo numeros por cada letra
for l in letras:
    for n in numeros:
        print(f'letra: {l} numero: {n}')
        