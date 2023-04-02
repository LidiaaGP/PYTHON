class Alumno:
    
    def __init__(self,DNI,nombre,direccion,telefono):
        self.__DNI=DNI
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono

    def get_dni(self):
        return self.__DNI

    def get_nombre(self):
        return self.__nombre

    def get_direccion(self):
        return self.__direccion

    def get_telefono(self):
        return self.__telefono

    def set_dni(self, value):
        self.__DNI = value

    def set_nombre(self, value):
        self.__nombre = value

    def set_direccion(self, value):
        self.__direccion = value

    def set_telefono(self, value):
        self.__telefono = value

    def toString(self):
        return self.__DNI+" "+self.__nombre+" "+self.__direccion+" "+self.__telefono