# En JAVA un array es un conjunto de elementos del mismo tipo de tamaño predefinido
# En Python una lista es un conjunto de elementos

lista1=[5,9,8,12,14,12,32,67]
print(type(lista1))
print("Lista 1: ",lista1)

lista2=["Hola",6,9,"adios",True]
print("Lista 2",lista2)

lista3=["Hola",6,9,[8,12],"adios",True,["texto1","texto2"]]
print("Lista 3",lista3)

# Acceder a los elementos de una lista
print("Primer elemento lista 1:",lista1[0])
print("Cuarto elemento lista 2:",lista2[3])
print("Ultimo elemento lista 2:",lista2[len(lista2)-1])
print("Ultimo elemento lista 2:",lista2[-1])
print("2 elemento del 4 elemento lista 3:",lista3[3][1])

# Recorrido de listas

print("RECORRIDO LISTA 1:")
for i in range(0,len(lista1)):
    print(lista1[i])

print("RECORRIDO LISTA 2:")    
for elemento in lista2:
    print(elemento)

#sublistas
lista4=lista1[2:4]
print("Lista 4: ",lista4)  
lista5=lista1[2:8:2]
print("Lista 5: ",lista5)
    
# Ver si un elemento esta en la lista
numero=int(input("Dime numero a buscar: "))
if numero in lista1:
    print(numero,"esta en la lista en la posicion",lista1.index(numero))
else:
    print(numero,"no esta en la lista")
    
# Contar numero de apariciones de un elemento
numero=int(input("Dime numero: "))
print(numero," aparece ",lista1.count(numero)," veces")

#Añadir elementos a una lista
# añadir al final (append)
lista1.append(47)
print("Lista 1: ",lista1)

# añadir en una posicion (insert)
lista1.insert(2, 113)
print("Lista 1: ",lista1)

#Borrar elementos
numero=int(input("Dime numero a borrar: "))
lista1.remove(numero)
print("Lista 1: ",lista1)
    
    
    
    
    
    
