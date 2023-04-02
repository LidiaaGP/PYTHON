from Empleado import Empleado

class Programador(Empleado):
   
    def __init__(self,dni,nombre,salarioBruto,horasExtra,precioHoraExtra):
        super().__init__(dni,nombre,salarioBruto)
        self.__horasExtra=horasExtra
        self.__precioHoraExtra=precioHoraExtra
    
    def salarioneto(self):
        return super().salarioneto()+(self.__horasExtra*self.__precioHoraExtra)
    
    def toString(self):
        return super().toString()+" "+str(self.__horasExtra)+" "+str(self.__precioHoraExtra)