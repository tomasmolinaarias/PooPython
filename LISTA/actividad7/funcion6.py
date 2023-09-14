def funcion6(cantidad):
    lista = list()
    cont: int = 0
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

    print()

    promedio: float = sum(lista) / cantidad
    promedio_redondeado: float = round(promedio, 2)
    print("El promedio es", promedio_redondeado)
