# Trabajar con booleanos

boleano1=True
boleano2=False

# Operadores logicos and,or,not
resultadoand=boleano1 and boleano2
resultadoor=boleano1 or boleano2
resultadonot=not boleano1

print(boleano1,"and",boleano2,"=",resultadoand)
print(boleano1,"or",boleano2,"=",resultadoor)
print("not",boleano1,"=",resultadonot)

#Operadores comparacion <,<=,>,>=,==,!=
edad=int(input("Dime edad: "))
mayoredad=edad>=18
jubilado=edad>65
puedetrabajar=mayoredad and not jubilado
print("Puede trabajar: ",puedetrabajar)
