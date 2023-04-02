codigo=input("Dime el codigo EAN: ")
suma=0
for i in range(len(codigo)-2,-1,-1):
    digito=int(codigo[i])
    pos=len(codigo)-i-1
    if pos%2==0:
        suma=suma+digito
    else:
        suma=suma+digito*3

comprobacion=suma+int(codigo[-1])
if comprobacion%10==0:
    print("SI")
    if len(codigo)==8:
        print("EAN-8")
    elif len(codigo)==13:
        print("EAN-13")
        if (codigo[0]=='0'):
            print("EEUU")
        elif (codigo[0]=='3' and codigo[1]=='8' and codigo[2]=='0'):
            print("Bulgaria")
        elif (codigo[0]=='5' and codigo[1]=='0'):
            print("Inglaterra")
        elif (codigo[0]=='5' and codigo[1]=='3' and codigo[2]=='9'):
            print("Irlanda")
        elif (codigo[0]=='5' and codigo[1]=='6' and codigo[2]=='9'):
            print("Portugal")
        elif (codigo[0]=='7' and codigo[1]=='0'):
            print("Noruega")
        elif (codigo[0]=='7' and codigo[1]=='5' and codigo[2]=='9'):
            print("Venezuela")
        elif (codigo[0]=='8' and codigo[1]=='5' and codigo[2]=='0'):
            print("Cuba")
        elif (codigo[0]=='8' and codigo[1]=='9' and codigo[2]=='0'):
            print("India")
        else:
            print("Desconocido")
    else:
        print("Codigo incorrecto")
else:
    print("NO")
    