limit = int(input("INGRESE CUANTOS ELEMENTOS VA INGRESAR:\n→"))
conjunto = set()
for x in range(limit):
    b = str(input(f"INGRESA LA PALABRA Nº{x+1} :\n→"))
    conjunto.add(b)
print(f"EL CONJUNTO ES:\n{conjunto}")
