from ej5.excepciondni import excepciondni
from ej5.excepcionEdad import excepcionedad
from xml.etree.ElementTree import tostring
class persona:
    def __init__(self,dni,nombre,edad):
        self.__nombre=nombre
        if len(dni)!=9:
            raise excepciondni()
        else:
            self.__dni=dni
        if edad<0 or edad>120:
            raise excepcionedad()
        else:
            self.__nombre=nombre
            
    def toString(self):
        return str(self.__dni)+" "+self.__nombre+" "+str(self.__edad)
        