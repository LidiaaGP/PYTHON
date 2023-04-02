import datetime

class Persona:
    
    #Para hacer los atributos privados se pone __ antes del nombre del atributo
    def __init__(self,dni,nombre,anhoNacimiento=0):
        self.__dni=dni;
        self.__nombre=nombre;
        self.__anhoNacimiento=anhoNacimiento;

    def get_dni(self):
        return self.__dni

    def get_nombre(self):
        return self.__nombre

    def get_anho_nacimiento(self):
        return self.__anhoNacimiento

    def set_dni(self, value):
        self.__dni = value

    def set_nombre(self, value):
        self.__nombre = value

    def set_anho_nacimiento(self, value):
        self.__anhoNacimiento = value
    
    def edad(self):
        fechactual=datetime.datetime.now()
        anhoActuaL=fechactual.year
        return anhoActuaL-self.get_anho_nacimiento()

    def ver_datos(self):
        print("DNI:",self.get_dni(),"Nombre:",self.get_nombre(),"Anho Nacimiento:",self.get_anho_nacimiento()," Edad:",self.edad())

class CuentaBancaria:
    def __init__(self,titular,saldo=0):
        self.__titular=titular
        self.__saldo=saldo

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def set_titular(self, value):
        self.__titular = value

    def set_saldo(self, value):
        self.__saldo = value

    def ver_datos(self):
        self.get_titular().ver_datos()
        print("Saldo:",self.get_saldo())


persona1=Persona("11111111A","Pepito")
persona1.set_anho_nacimiento(2000)
cuenta1=CuentaBancaria(persona1,15)
cuenta1.ver_datos()

#Atributos dinamicos
persona1.altura=180
print("Altura:",persona1.altura)

