def filtro(cantidad, Pares, Impares):
    cont: int = 0
    while cont < cantidad:
        number = int(input(f"Ingresa El Número {cont+1}:\n"))
        if number % 2 == 0:
            Pares.append(number)
        else:
            Impares.append(number)
        cont += 1
