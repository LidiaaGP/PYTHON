def imposible(lado1,lado2,lado3):
    if ((lado1+lado2)<=lado3):
        resultado=True
    elif ((lado1+lado3)<=lado2):
        resultado=True
    elif ((lado2+lado3)<=lado1):
        resultado=True
    else:
        resultado=False
    return resultado

def cuadradomayor(lado1,lado2,lado3):
    if (lado2>lado1 and lado2>lado3):
        resultado=lado2*lado2
    elif (lado3>lado1 and lado3>lado2):
        resultado=lado3*lado3
    else:
        resultado=lado1*lado1
    return resultado

def sumacuadradosmenores(lado1,lado2,lado3):
    if (lado2>lado1 and lado2>lado3):
        resultado=lado1*lado1+lado3*lado3
    elif (lado3>lado1 and lado3>lado2):
        resultado=lado2*lado2+lado1*lado1
    else:
        resultado=lado2*lado2+lado3*lado3
    return resultado
    
lado1=float(input("Dime la longitud del lado 1: "))
lado2=float(input("Dime la longitud del lado 2: "))
lado3=float(input("Dime la longitud del lado 3: "))

if (imposible(lado1,lado2,lado3)):
    print("Imposible")
elif (cuadradomayor(lado1,lado2,lado3)==sumacuadradosmenores(lado1,lado2,lado3)):
    print("Rectangulo")
elif (cuadradomayor(lado1,lado2,lado3)>sumacuadradosmenores(lado1,lado2,lado3)):
    print("Obtusangulo")
else:
    print("Acutangulo")