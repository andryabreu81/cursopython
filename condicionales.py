## condicionales if elif else
# Condicionales

a = 5
b = 2
c = 3

if a > b:
    print("a es mayor que b")
elif c < b:
    print("c es menor que b")
else:
    print("a es igual a c")
# condicionales if, elif, else

a=5
b=15
c=10

if (a > b):
    print ('a es mayor que b')
elif (b > c):
    print ('b es menor que c')
elif (a == c):
    print ('a es igual a c')

# ejemplo practico

# objetivo entrar al boliche
print('practica: entrar al boliche')
edad = 61
print(f'Edad: {edad}')

if (edad >= 18 and edad <= 60):
    print ('Si puedes entrar al boliche!')
else:
    if (edad < 18):
        print ('No tienes edad para entrar al boliche')
    else:
        print ('Este boliche solo acepta personas hasta 60 anios')

## shorthands, condicionales de una sola linea
print('ejemplo de codiciones shorthands')

d=7
e=20
f=10

if (d > e): print(f'{d} es mayor que {e}')

print('e es mayor que d') if e > d else print('d es mayor que e')

        