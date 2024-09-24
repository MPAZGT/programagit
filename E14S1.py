#números pares de una lista#
lista = [5, 1, 2, 10, 12]
# con la sig sentencia le decimos que recorra cada elemento de la lista#
for numeros in lista:
    if numeros % 2 == 0:
        print(numeros)