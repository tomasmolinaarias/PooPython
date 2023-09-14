from funcion13 import funcion
lista = []
cantidad = int(input("Ingresa la cantidad de numeros que vas ingresar:\n"))
if cantidad > 1:
    funcion(cantidad, lista)
else:
    print("La cantidad tiene que ser mayor a 1")
