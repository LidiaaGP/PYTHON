class Persona:
    
    def __init__(self,DNI,nombre,edad):
        self.__DNI=DNI
        self.__nombre=nombre
        self.__edad=edad

    def get_dni(self):
        return self.__DNI


    def get_nombre(self):
        return self.__nombre


    def get_edad(self):
        return self.__edad


    def set_dni(self, value):
        self.__DNI = value


    def set_nombre(self, value):
        self.__nombre = value


    def set_edad(self, value):
        self.__edad = value

    
    def toString(self):
        return "DNI: "+self.__DNI+" Nombre: "+self.__nombre+" Edad: "+str(self.__edad)

  
    
    