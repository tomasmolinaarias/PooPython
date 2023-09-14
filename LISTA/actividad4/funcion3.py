def funcion3(cont, lista):
    print("Tienes que ingresar 5 Palabras\n")
    while cont < 5:
        pal = str(input(f"Ingrese la {cont+1} palabra:\n"))
        lista.append(pal)
        cont += 1
    print()
    print("Lista Vertical:")
    for x in lista:
        print(x)
