import uuid
PRODUCTO = dict()

id_aleatorio = str(uuid.uuid4())
for c in range(4):
    if c+1 == 1:
        x = print("SE INGRESO CODIGO")
        PRODUCTO["CODIGÓ"] = id_aleatorio
    elif c+1 == 2:
        x = str(input("\nINGRESE SU NOMBRE\n→"))
        PRODUCTO["NOMBRE"] = x
    elif c+1 == 3:
        x = int(input("\nINGRESE SU PRECIO\n→"))
        PRODUCTO["PRECIO"] = x
    else:
        x = input("\nINGRESE SU STOCK\n→")
        PRODUCTO["STOCK"] = x


print(PRODUCTO)
