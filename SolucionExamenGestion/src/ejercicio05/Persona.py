from ExcepcionDNI import ExcepcionDNI
from ExcepcionEdad import ExcepcionEdad
class Persona:
    
    def __init__(self, nombre,dni,edad):
        self.__nombre=nombre
        if len(dni)!=9:
            raise ExcepcionDNI()
        else: 
            self.__dni=dni
        if edad<0 or edad>130:
            raise ExcepcionEdad()
        else:
            self.__edad=edad
        
    def toString(self):
        return self.__nombre+" "+self.__dni+" "+str(self.__edad)
        