from ejemplo01.Persona import Persona
from ejemplo01.Cliente import Cliente
from ejemplo01.Empleado import Empleado
from ejemplo01.Comercial import Comercial

persona1=Persona("11111111A","Pepito",30)
print(persona1.toString())

cliente1=Cliente("22222222B","Pedrito",30,0.12)
print(cliente1.toString())

empleado1=Empleado("33333333C","Paquito",30,1234)
print(empleado1.toString())

comercial1=Comercial("44444444D","Fulanito",30,900,0.3)
print(comercial1.toString())