
articulos=[]

for i in range(0,10):
    articulos.append(int(input("Dime precio ")))

suma=0
mayor_precio=articulos[0]
menor_precio=articulos[0]
contador=0

for j in articulos:
    suma=suma+j
    if j>mayor_precio:
        mayor_precio=j
    if j<menor_precio:
        menor_precio=j
    if j<30:
        contador=contador+1
media=suma/10

print(articulos)
print("mayor precio",mayor_precio)
print("menor precio",menor_precio)
print("precio medio",media)
print("hay",contador,"precios por debajo de 30 euros")
