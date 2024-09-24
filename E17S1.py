#suma de digitos#
numero = int(input("ingresar numero: "))
 
suma = 0
while numero > 0: 
    suma = suma + (numero % 10)
    numero = numero // 10
print("la suma de los digitos es: ",suma)
