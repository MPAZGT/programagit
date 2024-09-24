#numero factorial#
numero = int(input("ingrese el número: "))
fact = 1

for i in range(1, numero+1):
    fact = fact * i

print("El número factorial es : ", end="")
print(fact)