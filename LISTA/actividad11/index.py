from funcion10 import filtro

Positivos = []
Negativos = []
Neutros = []

for x in range(10):
    number = int(input(f"Ingresa El Número {x+1}:\n"))
    filtro(number, Positivos, Negativos, Neutros)
print()
print(f"La lista de Positivos:\n {Positivos}")
print(f"La lista de Negativos:\n {Negativos}")
print(f"La lista de Neutros:\n {Neutros}")
