def funcion2(cont, lista):
    print("Tienes que ingresar 5 numeros Enteros\n")
    while cont < 5:
        num = int(input(f"Ingrese el numero {cont + 1} enteros:\n"))
        lista.append(num)
        cont += 1
    print()
    print("Lista Vertical:")
    for x in lista:
        print(x)
