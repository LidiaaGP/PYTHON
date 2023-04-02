from Empleado import Empleado

class Comercial(Empleado):
   
    def __init__(self,dni,nombre,salarioBruto,ventas,porcentaje):
        super().__init__(dni,nombre,salarioBruto)
        self.__ventas=ventas
        self.__porcentaje=porcentaje
    
    def salarioneto(self):
        return super().salarioneto()+(self.__ventas*self.__porcentaje)
    
    def toString(self):
        return super().toString()+" "+str(self.__ventas)+" "+str(self.__porcentaje)
        