import numpy as np
e = int(input("INGRESA LAS CANTIDAD DE NOTA\n→"))
print("\n-----------------0------------------------")
print("RECUERDA QUE LA SEPARCION ES '.' EJ: 4.5")
print("SI INGRESA SOLO 4 SE COLOCARA COMO 4.0")
print("-----------------0------------------------\n")

notas = list()
conMaxima: int = 0
conMinima: int = 0
for c in range(e):
    nota = float(input("INGRESA LAS CANTIDAD DE NOTA\n→"))
    notas.append(nota)
    if nota > 4:
        conMaxima += 1
    elif nota < 4:
        conMinima += 1

arregloNotas = np.array(notas)
promedio: int = arregloNotas.sum()/len(arregloNotas)
print("-----------------0------------------------")
print(f"LA NOTA NOTA MINIMA ES : \n{arregloNotas.min()}")
print("-----------------0------------------------")
print(f"LA NOTA NOTA MAXIMA ES : \n{arregloNotas.max()}")
print("-----------------0------------------------")
print(f"EL PROMEDIO ES :\n{promedio}")
print("-----------------0------------------------")
print(f"CANTIDAD DE NOTAS MAYOR A 4 :\n{conMaxima}")
print("-----------------0------------------------")
print(f"CANTIDAD DE NOTAS MENOR A 4 :\n{conMinima}")
print("-----------------0------------------------")
