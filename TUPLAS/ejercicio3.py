lista = list(range(101))
for x in lista:
    if x % 2 == 0:
        lista.remove(x)
tupla = tuple(lista)
print(f"LA TUPLA ES \n {tupla}")
