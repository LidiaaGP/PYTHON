pisoinicial=int(input("Piso inicial: "))
pisodestino=int(input("Dime piso: "))
suma=0;
if pisodestino>=0:
    suma=suma+abs(pisodestino-pisoinicial)
if (pisodestino!=1):
    pisoinicial=pisodestino
    pisodestino=int(input("Dime piso"))
    if pisodestino>=0:
        suma=suma+abs(pisodestino-pisoinicial)
print(suma)