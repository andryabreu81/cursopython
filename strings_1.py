# tipos de datos string
from math import e


datos = 'esto es, una cadena de texto, mucho mas larga'
datos2 = "esto es una cadena de texto adicional"
datos3 = '''esto es una cadena de texto'''

#imprimir un caracter de un string

caracter = datos[1] # seleccionamos el caracter por el indice, como un array
print(caracter)# imprime la lerta s

# para determinar el lergo de un string
largo1 = len(datos) # largo de la cadena
print(largo1) # imprime 27
largo2 = len(datos2) # largo de la cadena
print(largo2) # imprime 37
# para determinar el tipo de dato
tipo = type(datos) # tipo de dato
print(tipo) # imprime <class 'str'> 

#determinar si un string esta dentro de otro string
print("cadena" in datos) # imprime True
print("cadena".lower() in datos.lower()) # imprime True
print("cadena" not in datos) # imprime False

# convertir un string a mayusculas
mayusculas = datos.upper() # convierte a mayusculas 
print(mayusculas)
minusculas = datos.lower() # convierte a minusculas
print(minusculas) # imprime en minusculas

# imprimir parte de un string
print(datos[10:18])# imprime a cadena
print(datos[10:])# imprime a cadena de texto, desde el 10 hasta el final
print(datos[:10])# imprime esto es una cadena de texto desde el inicio hasta el 10
print(datos[-1])# imprime el ultimo caracter de la cadena
print(datos[-10:])# imprime una cadena de texto

# texto sin espacios
print(datos.strip()) # elimina los espacios al inicio y al final de la cadena
print(datos.lstrip()) # elimina los espacios al inicio de la cadena 

# reemplazo
reemplazo = datos.replace("cadena", "strings") # reemplaza la palabra cadena por strings
print(reemplazo) # imprime esto es una strings de texto

# separar por comas
separar = datos.split(",") # separa la cadena por comas
print(separar) # imprime ['esto es', ' una cadena de texto', ' mucho mas larga']

# f-strings, permite imprimir string de varios tipos
nombre = "Juan"
apellido = "Perez"
edad = 30
fstrings = f"Hola, mi nombre es {nombre} {apellido} y tengo {edad} años"
print(fstrings) # imprime Hola, mi nombre es Juan Perez y tengo 30 años
fstrings = f"Hola, mi nombre es {nombre.lower()} {apellido.upper()} y tengo {edad:.2f} años"
print(fstrings) # imprime Hola, mi nombre es juan PEREZ y tengo 30.00 años

# calculos
resultado = f"la suma de 5 + 25 es {5+25}" # imprime la suma de 5 + 25 es 30
print(resultado)

# iniciales con mayusculas
iniciales = datos.capitalize()# solo la primera letra del string
print(iniciales)

iniciales = datos.title()# iniciales en mayusculas de cada palabra de un string
print(iniciales)

contar = datos.count('a')   # cuenta la cantidad de veces que aparece la letra a
print(contar)

# buscar un texto
buscar = datos.find('cadena')# indica en que pocision del string esta ese texto
print(buscar)