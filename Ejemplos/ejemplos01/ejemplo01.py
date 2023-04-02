# Tipos en Python
from pickle import TRUE

# Python utiliza tipado dinamico

numero1=5
numero2=5.7
mensaje="Hola"
booleano1=True

# Para mostrar funcion print
# En la funcion print usamos , para concatenar
# Para saber el tipo de una variable se usa la funcion type

print(numero1,"es de tipo",type(numero1))
print(numero2,"es de tipo",type(numero2))
print(mensaje,"es de tipo",type(mensaje))
print(booleano1,"es de tipo",type(booleano1))

#Permite cambiar el tipo de una variable dinamicamente
numero1="Adios"
print(numero1,"es de tipo",type(numero1))

#En Python no existen constantes. Por convencion se usan mayusculas en los nombres
PI=3.14159
print(PI,"es de tipo",type(PI))

