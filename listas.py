# listas: coleccion (array) permiten almacenar multiples elementos en una misma variable

frutas = ['naranjas','manzanas','peras','kiwis','mangos']
print(frutas)# imprime la lista
print(type(frutas))# imprime el tipo de dato
print(len(frutas))# imprime la longitud de la lista
print(frutas[0])# imprime el primer elemento de la lista

print('lista desde un constructor')
listaconstructor = list(('naranjas','manzanas','peras','kiwis','mangos'))
print(listaconstructor)# imprime la lista
parteLista = listaconstructor[0:2]# imprime parte de la lista
print(parteLista)# imprime parte de la lista
print(parteLista := listaconstructor[0:3])# imprime parte de la lista

# como cambiar los datos de una lista
tecnologias = ['PHP','Python','Angular','Java','JavaScript','SQL']
print(tecnologias)# imprime la lista
tecnologias[0] = 'C#' # cambia el primer elemento de la lista
print(tecnologias)

# insertar un nuevo elemento en una lista
tecnologias.insert(0, 'C++') # inserta un nuevo elemento en la lista
print(tecnologias)# imprime la lista

# agregar un nuevo elemento al final de la lista
tecnologias.append('Ruby') # agrega un nuevo elemento al final de la lista
print(tecnologias)# imprime la lista

# agregar un nuevo elemento en una posicion especifica de la lista
tecnologias.insert(2, 'Swift') # agrega un nuevo elemento en la posicion 2 de la lista
print(tecnologias)# imprime la lista

# eliminar un elemento de la lista
tecnologias.remove('C#') # elimina el elemento C# de la lista
print(tecnologias)# imprime la lista

# eliminar un elemento de la lista por su posicion
tecnologias.pop(0) # elimina el elemento de la posicion 0 de la lista
print(tecnologias)# imprime la lista

# eliminar un elemento de la lista por su valor
tecnologias.remove('Java') # elimina el elemento Java de la lista
print(tecnologias)# imprime la lista

# agregar una lista dentro de otra lista
tecnologias2 = ['C#','C++','Java','JavaScript','SQL']
tecnologias.append(tecnologias2) # agrega la lista tecnologias2 a la lista tecnologias
print(tecnologias)# imprime la lista

# agregar una lista dentro de otra lista
tecnologias.extend(tecnologias2) # agrega la lista tecnologias2 a la lista tecnologias
print(tecnologias)# imprime la lista

# recorrer una lista con un for
for tecnologia in tecnologias:
    print(tecnologia)# imprime la lista

# recorrer una lista con un for y un range
print('recorrido de la lista con un for y un range')
for i in range(len(tecnologias)):
    print(f"{i+1}. {tecnologias[i]}")# imprime la lista

# recorrer una lista con un for y un range y un paso de 2
for i in range(0, len(tecnologias), 2):
    print(tecnologias[i])# imprime la lista

# recorrer una lista con un for y un range y un paso de -1
for i in range(len(tecnologias)-1, -1, -1):
    print(tecnologias[i])# imprime la lista

# shorthands
[print(tecnologia) for tecnologia in tecnologias]

print('muestra solo los elementos q tengas un string especifico')
# imprimir los elementos q tengas un valor especifico
for tecnologia in tecnologias:
    if 'n' in tecnologia:
        print(tecnologia)# imprime la lista

# ordenar los elementos de una lista
tecnologias2.sort() # ordena la lista de manera ascendente
print(tecnologias2)

tecnologias2.sort(reverse=True) # ordena la lista de manera descendente
print(tecnologias2)
tecnologias2.reverse()
print(tecnologias2)