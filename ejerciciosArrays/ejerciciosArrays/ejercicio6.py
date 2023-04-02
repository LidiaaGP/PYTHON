array=[]
contador=0
for i in range(0,10):
    array.append(int(input("Dime numero ")))
    
numero=int(input("Dime numero a buscar "))

for j in array:
    if j==numero:
        contador=contador+1
        
print(numero,"esta en la lista",contador,"veces")
    