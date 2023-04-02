numero1=float(input("Dime numero 1: "))
numero2=float(input("Dime numero 2: "))
numero3=float(input("Dime numero 3: "))
if numero1>numero2 and numero1>numero3:
    print(numero1,"es el mayor")
elif numero2>numero1 and numero2>numero3:
    print(numero2,"es el mayor")
else:
    print(numero3,"es el mayor")