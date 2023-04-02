import math
a=int(input("Dime a: "))
b=int(input("Dime b: "))
c=int(input("Dime c: "))
x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
print("Solucion 1: ",x1)
print("Solucion 2: ",x2)