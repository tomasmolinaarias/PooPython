limit = int(input("INGRESE CUANTOS ELEMENTOS VA INGRESAR:\n→"))
conjunto = set()
for x in range(limit):
    b = int(input(f"INGRESA NUMERO Nº{x+1} :\n→"))
    conjunto.add(b)
print(f"EL CONJUNTO ES:\n{conjunto}")
