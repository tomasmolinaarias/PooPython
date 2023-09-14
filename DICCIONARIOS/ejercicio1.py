DATOS_PERSONAL = dict()
for c in range(4):
    if c+1 == 1:
        x = str(input("INGRESE SU NOMBRE\n→"))
        DATOS_PERSONAL["NOMBRE"] = x
    elif c+1 == 2:
        x = str(input("\nINGRESE SU DIRECCIÓN\n→"))
        DATOS_PERSONAL["DIRECCIÓN"] = x
    elif c+1 == 3:
        x = int(input("\nINGRESE SU EDAD\n→"))
        DATOS_PERSONAL["EDAD"] = x
    else:
        while True:
            x = input("\nINGRESE SU TELEFONO\n→")
            if x.isdigit() and len(x) == 9:
                print("\nINGRESA EL 9 ANTES DEL NUMERO\n")
                DATOS_PERSONAL["TELEFONO"] = x
                break
            else:
                print("Por favor, ingrese un número de teléfono válido de 9 dígitos.")

print(DATOS_PERSONAL)
