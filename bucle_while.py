# bucles loops con while
print('ejemplos de bucles')
n = 1

while (n <= 10):
    print(f'n: {n}')
    n = n + 1
    

print('2do ejemplo, se detiene cuando x llegue a 5')

x = 1
while (x < 10):
    print(f'x: {x}')
    if (x == 5):
        break
    x = x + 1

print('3er ejemplo, se detiene cuando ya no cumple la condicion')

c = 0
while (c < 10):
    c = c + 1
    if (c == 5):
        continue # continue mata el proceso en 5 y luego continua hasta q c sea igual a 10
    print(f'c: {c}')
else:
    print('sale del bucle porq c ya no es menos o igual a 10')

print('4to ejemplo, bucle infinito')

while (True):
    respuesta = input('Desea salir? (s/n): ').strip().lower()
    if (respuesta == 's'):
        print('Saliendo del bucle')
        break
    elif (respuesta == 'n'):
        print('Continuando...')
    else:
        print('Respuesta no valida')
        break
    