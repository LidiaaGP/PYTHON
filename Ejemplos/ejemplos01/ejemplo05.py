# Trabajar con textos

texto1=input("Dime texto 1: ")

print("Longitud: ",len(texto1))
print("Primer caracter: ",texto1[0])
print("Ultimo caracter: ",texto1[len(texto1)-1])
print("Ultimo caracter: ",texto1[-1])
print("Penultimo Caracter: ",texto1[-2])
print("Substring 3 primeras letras: ",texto1[0:3])

texto2=input("Dime texto 2: ")

# Concatenar +
concatenar=texto1+"\n"+texto2
print("Concatenado:",concatenar)

#Repetir
repetido=texto2*3
print("Repetido:",repetido)
