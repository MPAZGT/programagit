#contar vocales#
cadena = input("Ingrese una cadena de texto: ")
vocales = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
#iniciar conteo#
contar_vocales= 0

for x in cadena:
    if x in vocales:
        contar_vocales += 1

print('Total vocales:', contar_vocales)