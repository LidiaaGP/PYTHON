from ej5.excepcionEdad import excepcionedad
from ej5.excepciondni import excepciondni
from ej5.persona import persona
try:
    nombre=input("Dime nombre ")
    edad=input("Dime edad ")
    dni=input("Dime dni ")
    persona1=persona(dni, nombre, edad)
    print(persona1)
except excepciondni as dni:
    print(dni.getmensaje())
