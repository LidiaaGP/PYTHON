lado=int(input("Tamaño lado hexagono: "))
caracter=input("Caracter: ")[0]

for i in range(0,lado):
    for j in range(1,(lado-i)):
        print(" ",end="")
    for j in range(1,(lado+i*2)+1):
        print(caracter,end="")
    print("")
for i in range((lado-2),-1,-1):
    for j in range(1,(lado-i)):
        print(" ",end="")
    for j in range(1,(lado+i*2)+1):
        print(caracter,end="")
    print("")