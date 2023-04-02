from ejercicio02.Vehiculo import Vehiculo

vehiculo1=Vehiculo()
vehiculo1.marca="Seat"
vehiculo1.modelo="Ibiza"
vehiculo1.color="Rojo"
vehiculo1.num_ruedas=4

vehiculo2=Vehiculo()
vehiculo2.marca="Yamaha"
vehiculo2.modelo="MT-03"
vehiculo2.color="Negro"
vehiculo2.num_ruedas=2

print(vehiculo1.marca,vehiculo1.modelo,vehiculo1.color,vehiculo1.num_ruedas)
print(vehiculo2.marca,vehiculo2.modelo,vehiculo2.color,vehiculo2.num_ruedas)
vehiculo1.precio=11500
vehiculo2.precio=6000
print("Precio IVA vehiculo1:",vehiculo1.precio_IVA())
print("Precio IVA vehiculo2:",vehiculo2.precio_IVA())

