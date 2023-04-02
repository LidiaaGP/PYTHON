from ej4.empleado import empleado
class programador(empleado):
    def __init__(self,dni,nombre,salariobruto,horasextra,preciohoraextra):
        super().__init__(dni, nombre, salariobruto)
        self.__horasextra=horasextra
        self.__preciohoraextra=preciohoraextra
    
    def salarioneto(self):
        return super().salarioneto()+(self.__horasextra*self.__preciohoraextra)
    
    def toString(self):
        return super().toString()+" "+str(self.__horasextra)+" "+str(self.__preciohoraextra)