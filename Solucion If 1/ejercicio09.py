tipo_vehiculo=input("Dime vehiculo: ").lower()

if tipo_vehiculo=="bicicleta":
    print("Importe: 1 €")
elif tipo_vehiculo=="moto" or tipo_vehiculo=="coche":
    km=float(input("Dime km: "))
    importe=km*0.25
    print("importe:",importe)
elif tipo_vehiculo=="camion":
    km=float(input("Dime km: "))
    toneladas=float(input("Dime toneladas: "))
    importe=km*0.25+0.15*toneladas
    print("importe:",importe)
else:
    print("Vehiculo equivocado")