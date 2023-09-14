import numpy as np
lista = list(range(1, 101))
for x in lista:
    if x % 2 == 0:
        lista.remove(x)
arreglo = np.array(lista)
print(f"EL ARREGLO ES \n {arreglo}")
