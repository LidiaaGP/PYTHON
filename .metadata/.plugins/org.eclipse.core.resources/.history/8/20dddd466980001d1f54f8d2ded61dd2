from ejemplo01.Persona import Persona

class Empleado(Persona):

    def __init__(self,DNI,nombre,edad,salario):
        super().__init__(DNI,nombre,edad)
        self.__salario=salario

    def get_salario(self):
        return self.__salario


    def set_salario(self, value):
        self.__salario = value

    def toString(self):
        return super().toString()+" Salario: "+str(self.__salario)
    