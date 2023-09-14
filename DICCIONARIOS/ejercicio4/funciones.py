

def buscador(DATOS_PERSONAL):
    condicion = True
    print("INGRESA LO QUE ESTA BUSCADO")
    print("------------0--------------")
    print("INGRESA 1 SI BUSCA EL NOMBRE")
    print("INGRESA 2 SI BUSCA DIRECCIÓN")
    print("INGRESA 3 SI BUSCA LA EDAD")
    print("INGRESA 4 SI BUSCA EL TELEFONO")
    print("INGRESA 5 PARA SALIR")
    print("------------0--------------")
    while condicion == True:
        x = int(input("\n→"))
        if x == 1:
            print(f" EL NOMBRE ES :\n {DATOS_PERSONAL['NOMBRE']}")
        elif x == 2:
            print(f" LA DIRECCIÓN ES :\n {DATOS_PERSONAL['DIRECCIÓN']}")
        elif x == 3:
            print(f" LA EDAD ES :\n {DATOS_PERSONAL['EDAD']}")
        elif x == 4:
            print(f" EL TELEFONO ES :\n {DATOS_PERSONAL['TELEFONO']}")
        elif x == 5:
            print(f" GRACIAS CHAO!!!")
            condicion = False
        else:
            print("EL NUMERO INGRESADO ES INCORRECTO")
            continue
