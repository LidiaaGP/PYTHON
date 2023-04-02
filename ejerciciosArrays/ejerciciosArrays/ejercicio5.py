

numero=int(input("Dime numero de alumnos: "))
lista1=[numero]
nota=[]

for i in range(0,numero,1):
    nota.append(int(input("Dime nota: ")))

suma=0
minimo=nota[0]
maximo=nota[0]

for j in nota:
    suma=suma+j
    if(j>maximo):
        maximo=j
    if(j<minimo):
        minimo=j
media=suma/numero

print("media",media)
print("maximo",maximo)
print("minimo",minimo)