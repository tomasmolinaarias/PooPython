def funcion4(condicion, lista):
    print("=======================")
    print("almacen de numeros Enteros")
    print("----------o------------")
    print("para parar de almacenar ponga ( -99 )\n")
    print("=======================")
    while condicion == True:
        number = int(input("Ingrese numeros Enteros:\n"))
        if number != -99:
            lista.append(number)
        else:
            condicion = False
    print()
    print(f"El primero de la lista es {lista[0]}")
    print(f"El ultimo de la lista es {lista[len(lista)-1]}")
    print(f"Cantidad de elementos de la lista es {len(lista)}")
