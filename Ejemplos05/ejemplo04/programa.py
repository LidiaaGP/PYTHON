from ejemplo04.Persona import Persona
from ejemplo04.ExcepcionDNI import ExcepcionDNI

try:
    DNI=input("Dime DNI: ")
    nombre=input("Dime Nombre: ")
    edad=int(input("Dime edad: "))
    persona1=Persona(DNI,nombre,edad)
    print(persona1.toString())
except ExcepcionDNI as ex:
    print(ex.get_mensaje())
except Exception:
    print("ERROR GENERAL")
else: # Se ejecuta si no hay error
    print("NO ERROR")
finally: #Se ejecuta siempre
    print("FIN")