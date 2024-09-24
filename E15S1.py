#tablas de multiplicar#
numero = int(input("ingrese el número a multiplicar: "))
rango = range(1,10)

for valor in rango:
    mult = numero * valor 
    print(numero, '*' ,  valor, "=", mult)
