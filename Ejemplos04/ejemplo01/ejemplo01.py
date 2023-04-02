class Prueba1:
    
    #constructor sin parametros
    def __init__(self):
        self.atributo1="Valor por defecto"
        print("Constructor sin parametros clase Prueba1")

class Prueba2:
    #constructor con parametros
    def __init__(self,atributo2):
        self.atributo2=atributo2
        print("Constructor con parametros clase Prueba2")


class Persona:
    #constructor con parametros y valores por defecto
    def __init__(self,dni="",nombre=""):
        self.dni=dni
        self.nombre=nombre


prueba1=Prueba1()
print(prueba1.atributo1)

prueba2=Prueba2("Valor atributo 2")
print(prueba2.atributo2)

persona1=Persona()
print("DNI Persona 1:",persona1.dni)

persona2=Persona("11111111A")
print("DNI Persona 2:",persona2.dni)
persona3=Persona("22222222B","Pepito")
print("DNI Persona 3:",persona3.dni)
print("Nombre Persona 3:",persona3.nombre)

