#Programa que sume 5 numeros

print("SUMAR 5 NUMEROS. BUCLE FOR")
suma=0
for i in range(5):
    numero=int(input("Dime numero: "))
    suma=suma+numero
print("Suma: ",suma)

print("SUMAR 5 NUMEROS. BUCLE WHILE")
suma=0
i=0
while i<5:
    numero=int(input("Dime numero: "))
    suma=suma+numero
    i+=1
print("Suma: ",suma)


