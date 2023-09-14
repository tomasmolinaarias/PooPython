def funcion5(condicion, lista):
    print("=======================")
    print("almacen de Palabras")
    print("----------o------------")
    print("para parar de almacenar ponga (stop)\n")
    print("=======================")
    while condicion == True:
        palabra = str(input("Ingrese la palabra:\n"))
        if palabra.lower() != "stop":
            lista.append(palabra)
        else:
            condicion = False
    print()
    print(f"El primero de la lista es {lista[0]}")
    print(f"El ultimo de la lista es {lista[len(lista)-1]}")
    print(f"Cantidad de elementos de la lista es {len(lista)}")
