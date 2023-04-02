from ej4.empleado import empleado
from ej4.comercial import comercial
from ej4.programador import programador


comercial1=comercial("3454g", "pepe", 1200, 400, 12)
programador1=programador("344546h", "edsfdsg", 2000,4545, 45)
empleado1=empleado("32455y", "sfd", 3445)

print(comercial1.toString())
print(programador1.toString())
print(empleado1.toString())