#hacer caja registradora# ingresar nombre, cantidad y precio. Debe dar el total aplicar descuestos si los tiene y dar recibo.
def mostrar_menu():
    print("bienvenido a la Caja Registradora")
    print("1. Agregar producto")
    print("2. Agregar cantidad")
    print("3. Mostrar total")
    print("4. Salir")

def agregar_producto(carrito):
    producto = input("ingrese el nombre del producto: ")
    cantidad = int(input("ingrese cantidad: "))
    precio = float(input("ingrese el precio del producto: "))
    valor_total = cantidad * precio
    carrito.append(valor_total) 
    print(f"{producto} agregado al carrito por ${precio}, subtotal {valor_total}") 
def valor_total(carrito):
    valor_total == valor_total
def mostrar_total(carrito):
    total = sum(valor_total[1] for item in carrito)
    print(f"total a pagar: ${total:.2f}")

def main():
    carrito = []
    while True:
        mostrar_menu()
        opcion = input("selecciones una opcion: ")

        if opcion == "1":
            agregar_producto(carrito)
        elif opcion == "2":
            valor_total()
        elif opcion == "3":
            mostrar_total(carrito)
        elif opcion == "4":
            print("Gracias por utilizar la caja registradora. !Hasta luego!")
            break
        else:
            print("opcion invalida. Por favor, seleccione una opción valida")
if __name__ == "__main__":
    main()
