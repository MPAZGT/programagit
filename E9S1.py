#Núm máyor#
n1 = int(input("ingrese el primer número: "))
n2 = int(input("ingrese el segundo número: "))
n3 = int(input("ingrese el tercer número: "))

if n1 == n2 == n3 :
    print("los números son iguales")
elif n1 > n2 and n1 > n3:
    print(f"el número mayor es: {n1}")
elif n2 > n1 and n2 > n3:
    print(f"el número mayor es: {n2}")
else:
    print(f"el número mayor es: {n3}")