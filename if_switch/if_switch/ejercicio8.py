numero1=float(input("Dime numero 1: "))
numero2=float(input("Dime numero 2: "))
if (numero1>numero2 and numero1%numero2==0) or (numero2>numero1 and numero2%numero1==0):
    print("Son divisores")
else:
    print("No son divisores")