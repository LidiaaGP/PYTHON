from Persona import Persona
from ExcepcionDNI import ExcepcionDNI
from ExcepcionEdad import ExcepcionEdad

try:
    nombre=input("Dime nombre: ")
    dni=input("Dime DNI: ")
    edad=int(input("Dime edad: "))
    persona1=Persona(nombre,dni,edad)
    nombre=input("Dime nombre: ")
    dni=input("Dime DNI: ")
    edad=int(input("Dime edad: "))
    persona2=Persona(nombre,dni,edad)
    print(persona1.toString())
    print(persona2.toString())
except ExcepcionDNI as edni:
    print(edni.get_mensaje())
except ExcepcionEdad as eedad:
    print(eedad.get_mensaje())