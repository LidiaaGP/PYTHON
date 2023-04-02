sueldo=[]

for i in range(0,12):
    sueldo.append(int(input("Dime sueldo ")))
print(sueldo)
contador=0
for i in range(0,12):
    if sueldo[i]<800:
        sueldo[i]=sueldo[i]+100
        contador=contador+1
for j in sueldo:
    print(j)
print("el sueldo se actualiza",contador,"veces")