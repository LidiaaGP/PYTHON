numero1=float(input("Dime numero 1: "))
numero2=float(input("Dime numero 2: "))
numero3=float(input("Dime numero 3: "))

if numero1<numero2 and numero1<numero3:
    print("Menor:",numero1)
elif numero2<numero1 and numero2<numero3:
    print("Menor:",numero2)
else:
    print("Menor:",numero3)