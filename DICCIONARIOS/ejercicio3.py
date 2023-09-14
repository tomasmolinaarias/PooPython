
numeros_en_palabras = {
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco",
    6: "seis",
    7: "siete",
    8: "ocho",
    9: "nueve",
    10: "diez"
}
for numero in range(10):
    palabra = numeros_en_palabras[numero+1]
    print(f"{numero+1} --> {palabra}")
