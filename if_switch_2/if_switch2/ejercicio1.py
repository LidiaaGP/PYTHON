moneda=str(input("Dime moneda: "))
cantidad=float(input("Dime cantidad: "))
if moneda=="peseta":
    print(cantidad,"pesetas son",cantidad*0.006,"euros")
elif moneda=="euro":
    print(cantidad,"euros son",cantidad*166.386,"pesetas")
else:
    print("valor equivocado")
