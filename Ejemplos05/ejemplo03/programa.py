try:
    numero1=float(input("Dime numero 1: "))
    numero2=float(input("Dime numero 2: "))

    division=numero1/numero2

    print("Division:",division)

except ZeroDivisionError as ex:
    tb=ex.exc_info()[0]
    print(tb)
    print("No se puede dividir por cero")
except Exception:
    print("Error general")
