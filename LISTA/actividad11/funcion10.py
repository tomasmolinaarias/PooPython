def filtro(number, Positivos, Negativos, Neutros):
    if number > 0:
        Positivos.append(number)
    elif number < 0:
        Negativos.append(number)
    else:
        Neutros.append(number)
