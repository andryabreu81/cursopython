# operadores
a = 15
b = 30

# aritmeticos

suma = a+b
resta = a-b
mult = a*b
division = a/b # devuelve un valor con decimales
fDivision = a//b # devuelve un valor entero
resto = a % b # devuelve el resto de la divicion
expo = a**b # es decir 15 a la 30 

# de asignacion
x = 10
x += 5 # le suma 5 al anterior
x -= 2 # le resta 2 al anterior
x /= 10 # le divide 10 al anterior
x //= 10 # le divide 10 al anterior y devuelve un entero
x *= 10 # le multiplica 10 al anterior
x %= 10 # le devuelve el resto de la division entre 10
x **= 10 # le devuelve el resultado de la potencia entre 10
x = 10


# de comparacion
igual = a == b # devuelve True si son iguales
diferente = a != b # devuelve True si son diferentes
mayor = a > b # devuelve True si a es mayor que b
menor = a < b # devuelve True si a es menor que b
mayorIgual = a >= b # devuelve True si a es mayor o igual que b
menorIgual = a <= b # devuelve True si a es menor o igual que b

# de identidad
a = 10
b = 10
iguales = a is b
print(iguales)

iguales = a is not b
print(iguales)

# operadores logicos
edad = 17
tramite = edad >= 18 and edad <= 65
tramite = edad >= 18 or edad <= 65

# operadores de pertenencia
palabra = 'hola'
texto = 'hola mundo como estas'
pertenece =  palabra in texto
print(pertenece)

pertenece = palabra not in texto
print(pertenece)

