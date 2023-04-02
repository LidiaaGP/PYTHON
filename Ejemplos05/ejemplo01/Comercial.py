from ejemplo01.Empleado import Empleado

class Comercial(Empleado):
    
    def __init__(self,DNI,nombre,edad,salario,comision):
        super().__init__(DNI,nombre,edad,salario)
        self.__comision=comision

    def get_comision(self):
        return self.__comision

    def set_comision(self, value):
        self.__comision = value

    def toString(self):
        return super().toString()+" Comision: "+str(self.__comision)