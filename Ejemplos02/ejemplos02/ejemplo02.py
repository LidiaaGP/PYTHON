#Programa que diga si un numero es positivo, negativo o cero

numero=int(input("Dime un numero: "))

print("OPCION 1:")

if numero>0:
    print(numero,"es positivo")
else:
    if numero<0:
        print(numero,"es negativo")
    else:
        print(numero,"es cero")

print("\nOPCION 2:")

if numero>0:
    print(numero,"es positivo")
elif numero<0:
    print(numero,"es negativo")
else:
    print(numero,"es cero")

print("FIN")