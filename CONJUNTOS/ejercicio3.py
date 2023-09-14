limit = int(input("INGRESE CUANTAS NOTAS VA INGRESAR:\n→"))
conjunto = set()


def Instructivo():
    print("PARA INGRESA LAS NOTA LA SEPARACION ES CON '.' EJ: 4.5\n")
    print("SI COLOCA UN 4 SERA UN 4.0\n")


Instructivo()
for x in range(limit):
    b = float(input(f"INGRESA LA NOTA Nº{x+1} :\n→"))
    conjunto.add(b)
print(f"EL CONJUNTO ES:\n{conjunto}")
