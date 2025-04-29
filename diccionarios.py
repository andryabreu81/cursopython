# diccionarios: una coleccion de pares clave:valor 
# desordeada y mutable
# dict (dictionary){}

diccionario = {
    "nombre":"andri javier",
    "apellido":"abreu raffo",
    "cedula":"15837503",
    "tecnologias":['python','angular','javascript','nodejs'],
    "direccion":{
        "calle":"bella vista",
        "edificio":"bloque 33",
        "ciudad":"Caracas"
    },
    "edad":43
}
print(diccionario)

# tipo de dato
print('1. tipo de dato')
print(type(diccionario))

print('2. longitud de un diccionario')
# longitud de un diccionario
print(len(diccionario))

print('3. ejemplo de constructor de un diccionario')
# constructor de un diccionario
consDiccionario2 = dict(nombre="andri", apellido="abreu")
print(consDiccionario2)

# como acceder a un diccionario
nombre = consDiccionario2['nombre']
apellido = consDiccionario2['apellido']
print(f'nombre: {nombre} {apellido}')
print('nombre:',nombre, apellido)

# ejemplo 2 para obtener el valor de una clave de un diccionario
nombre2 = consDiccionario2.get('nombre')
print(nombre2)

#lista las claves de un diccionario
print('4. claves')
keys = consDiccionario2.keys()
print(keys)

# lista los valores de un diccionario
print('5. valores')
values = consDiccionario2.values()
print(values)

print('6. items')
# items: nos decuelve una tupla de clave:valor en una lista
items = consDiccionario2.items()
print(items)
