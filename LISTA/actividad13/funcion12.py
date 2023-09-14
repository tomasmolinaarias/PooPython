def funcion12(cantidad, lista):
    cont: int = 0
    while cont < cantidad:
        numero = int(input(f"Ingresa El numero n°{cont+1}\n"))
        lista.append(numero)
        cont += 1

    print(f"\nLa lista es:\n {lista}\n")

    for i in range(len(lista)):
        if lista[i] < 0:
            lista[i] = abs(lista[i])

    print(f"La lista modificada es:\n {lista}")
