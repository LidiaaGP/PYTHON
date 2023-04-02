# Entrada de datos, funcion input
variable1=input("Dime variable 1: ")

# input siempre devuelve un str
print(variable1,"es de tipo",type(variable1))

# para ller o convertir entre distintos tipos se usan las funciones de conversion (int,float,str)
variable1=int(variable1)
print(variable1,"es de tipo",type(variable1))

numero1=int(input("Dime numero 1: "))
numero2=float(input("Dime numero 1: "))

print(numero1,"es de tipo",type(numero1))
print(numero2,"es de tipo",type(numero2))