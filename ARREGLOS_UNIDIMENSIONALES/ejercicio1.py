import numpy as np
vocales = []

vocales_string = 'aeiou'

for letra in vocales_string:
    vocales.append(letra)

arreglo = np.array(vocales)
print("Vocales:", arreglo)
