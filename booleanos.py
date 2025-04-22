# booleanos
a = True
b = False

# devuelven True cuando un booleano tiene contenido, de cualquier tipo
cadena = bool('hola mundo')
print(cadena)

num = bool(2025)
print(num)

arreglo = bool(['andry','abreu'])
print(arreglo)

diccionario =  bool({"nombre":"andry","apellido":"abreu"})
print(diccionario)

# cuando un booleanos devuelve False, cuando estan vacias o nulas
cadena2 = bool('')
print(cadena2)

num2 = bool(0)
print(num2)

arreglo2 = bool([])
print(arreglo2)

diccionario2 =  bool({})
print(diccionario2)