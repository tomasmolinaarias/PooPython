def creacionLista(cantidad):
    cont: int = 0
    lista = list()

    nota: int = 0

    while cont < cantidad:
        nota = float(input("Ingrese la nota (entre 1 y 7):\n"))

        if nota > 7.0:
            print("La nota no puede ser mayor a 7")
            continue
        elif nota < 1.0:
            print("La nota no puede ser menor a 1")
            continue

        lista.append(nota)
        cont += 1
    return lista


def menu():
    print("----------------------0----------------------------")
    print("si quieres buscar por posicion ingresa  P ")
    print("si quieres saber la posicion del la nota ingresa N ")
    print("----------------------0----------------------------")
    print("para salir ingresa ( . ) ")
    print("======================0============================")
    print()


def pos(lista):
    condi: bool = True
    menu()
    while condi == True:
        o = str(input(" inserte su seleccion: \n"))
        if o.lower() == "p":
            print(f"Las cantidades de notas es {len(lista)}")
            x = int(input("ingrese la posicion que busca:\n"))
            print("\n----------------------0----------------------------")
            print(
                f"La nota que se encuentra en esa posicion es {lista[x-1]}")
            print("----------------------0----------------------------")
            print()
            print()
            menu()
            print()

        elif o.lower() == "n":
            x = float(input("Ingrese la nota que busca (entre 1 y 7):\n"))
            if x in lista:
                indice = lista.index(x)
                print("\n----------------------0----------------------------")
                print(f"El elemento {x} se encuentra en el índice {indice}")
                print("----------------------0----------------------------")
                print()
                print()
                menu()
                print()
            else:
                print(f"El elemento {x} no está en la lista")
                continue
        if o == ".":
            condi = False
