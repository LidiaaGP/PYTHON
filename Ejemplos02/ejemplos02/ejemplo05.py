#Bucle FOR

for i in [0,1,2,3,4,5]:
    print(i,end=" ")

print()

for tipocasa in ["edificio","chalet","piso",56]:
    print(tipocasa,end=" ")

print()

for i in range(7): # i va de 0 a 6 de 1 en 1
    print(i,end=" ")

print()
    
for i in range(5,10): # i va de 5 a 9 de 1 en 1
    print(i,end=" ")

print()

for i in range(5,16,2): # i va de 5 a 15 de 2 en 2
    print(i,end=" ")

print()

for i in range(9,0,-1): # i va de 9 a 1 de 1 en 1
    print(i,end=" ")

print()

# recorrer un array
texto="HOLA"
for i in range(len(texto)):
    print(texto[i],end=" ")

print()
for i in range(len(texto)-1,-1,-1):
    print(texto[i],end=" ")

