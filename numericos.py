numero_entero = 5

numero_decimal = 5.14

numero_complejo = 2 + 2j

# imprime el tipo de variable
print(numero_entero, type(numero_entero))
print(numero_decimal, type(numero_decimal))
print(numero_complejo, type(numero_complejo))

if (type(numero_decimal)) == int:
    print("Es un entero")
elif (type(numero_decimal)) == float:
    print("Es un decimal")
elif (type(numero_complejo)) == complex:
    print("Es un complejo")
else:
    print("No es un tipo de dato numerico")

# casteo entre numeros
# de entero a decimal
numero = complex(numero_entero)
print(numero) # imprime 5.0

numero2 = complex(numero_entero)
print(numero2) # imprime 5+0j

numero3 = complex(numero_decimal)
print(numero3) # imprime 5.14+0j

# numeros random

import random

n_ramdom = random.randrange(0,50,10)
print(n_ramdom) # imprime numeros aleatorios de 10 en 10 entre el 0 y 50