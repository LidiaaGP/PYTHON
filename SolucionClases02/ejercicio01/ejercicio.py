from ejercicio01.Reloj import Reloj

reloj1=Reloj()
reloj1.marca="Casio"
reloj1.modelo="X-300"
reloj1.precio=100
reloj1.stock=10
reloj1.esDigital=True

reloj2=Reloj()
reloj2.marca="Rolex"
reloj2.modelo="J-5000"
reloj2.precio=400
reloj2.stock=5
reloj2.esDigital=False

suma=reloj1.precio+reloj2.precio
print("Suma: ",suma)

