notas_alumnos = {}

for i in range(2):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    notas = []
    for j in range(4):
        nota = float(input(f"Ingrese la nota {j + 1} para {nombre}: "))
        notas.append(nota)
    notas_alumnos[nombre.lower()] = notas

while True:
    consulta = input(
        "Ingrese el nombre del alumno para consultar sus notas (o 'q' para salir): ")
    if consulta.lower() == 'q':
        break
    elif consulta.lower() in notas_alumnos:
        notas_del_alumno = notas_alumnos[consulta]
        print(f"Notas de {consulta}: {notas_del_alumno}")
    else:
        print("El nombre del alumno no se encuentra en la lista.")
print(notas_alumnos)
