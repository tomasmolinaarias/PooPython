def creacionLista(cantidad):
    cont: int = 0
    lista = list()
    while cont < cantidad:
        nota = int(input(f"Ingrese El Numero Entero n°{cont + 1} :\n"))
        lista.append(nota)
        cont += 1
    return lista


def mostarNumber(lista):
    lista.sort()
    print(f"\nEl numero menor es: {lista[0]}")
    print(f"\nEl numero mayor es: {lista[len(lista)-1]}")
    print(f"\nLa lista es: {lista}")
