import numpy as np
lista = list()
c = True
while c == True:
    x = int(input(
        f"PARA SALIR Y MOSTAR EL ARREGLO COLOCA -99 :\nINGRESA LA PALBRA Nº{c+1}\n→ "))
    if x != -99:
        lista.append(x)
    else:
        c = False
lista.sort()
arreglo = np.array(lista)
print(f"\nEL ARREGLO ES : \n {arreglo}")
