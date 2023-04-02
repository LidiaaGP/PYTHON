tipo_vehiculo=input("Dime vehiculo: ").lower()
if tipo_vehiculo=="bicileta":
    print("1 €")
elif tipo_vehiculo=="moto" or tipo_vehiculo=="coche":
    km=float(input("Dime km: "))
    print("importe:",km*0.25)
elif tipo_vehiculo=="camion":
    km=float(input("Dime km: "))
    toneladas=float(input("Dime toneladas: "))
    print("importe",km*0.25+0.15*toneladas)
else:
    print("vehiculo equivocado")