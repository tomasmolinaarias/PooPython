import numpy as np
lista = list()
for c in range(6):
    x = str(input(f"INGRESA LA PALBRA Nº{c+1} :\n→ "))
    lista.append(x)
lista.sort(key=len)
arreglo = np.array(lista)
print(f"\nEL ARREGLO ES : \n {arreglo}")
print(f"EL ELEMENTO CON MENOR CANTIDAD ES : {arreglo[0]}")
print(f"EL ELEMENTO CON MAYOR CANTIDAD ES : {arreglo[-1]}")
