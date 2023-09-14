def funcion(cantidad, lista):
    positivos = []
    negativos = []
    cont: int = 0
    while cont < cantidad:
        number = int(input(f"Ingresa el numero n°{cont + 1}:\n"))
        lista.append(number)
        cont += 1
        for numero in lista:
            if numero >= 0:
                positivos.append(numero)
            else:
                negativos.append(numero)
    positivos = list(set(positivos))
    negativos = list(set(negativos))

    positivos.sort()
    negativos.sort(reverse=True)

    lista_ordenada = positivos + negativos

    print(f"\n Lista Normal: \n {lista} ")
    print(f"\n Lista Modificada: \n {lista_ordenada} ")


# como lo aria yo
""" 
def funcion(cantidad, lista):
    cont: int = 0
    while cont < cantidad:
        number = int(input(f"Ingresa el numero n°{cont + 1}:\n"))
        lista.append(number)
        cont += 1
    lista_ordenada = sorted(lista, key=lambda x: (x >= 0, abs(x)))
    print(f"\n Lista Normal: \n {lista} ")
    print(f"\n Lista Modificada: \n {lista_ordenada} ")
 """
