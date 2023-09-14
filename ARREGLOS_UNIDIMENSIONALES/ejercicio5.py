import numpy as np
lista = list()
for c in range(10):
    x = int(input(f"INGRESA EL NUMERO Nº{c+1} :\n→ "))
    lista.append(x)
arreglo = np.array(lista)
print(f"\nEL ARREGLO ES : \n {arreglo}")
print(f"EL PRIMER ELEMENTO ES : \n {arreglo[0]}")
print(f"EL ULTIMO ELEMENTO ES : \n {arreglo[-1]}")
