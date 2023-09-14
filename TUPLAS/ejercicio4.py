lista = list()
for x in range(5):
    PAL = str(input(f"INGRESE PALABRA Nº{x+1}:\n→"))
    lista.append(PAL)

tuplas = tuple(lista)
print(f"\nLA TUPLAS ES = {tuplas}")
