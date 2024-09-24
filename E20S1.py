#Contador de palabras#
frase = input("Ingrese una frase: ")
palabras = frase.split()
#iniciar conteo#
contar_palabras= 0

for x in palabras:
        contar_palabras += 1

print(contar_palabras)