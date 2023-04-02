from ejercicio02_03.Multimedia import Multimedia

class ListaMutimedia:
    
    __MAX=200
    
    def __init__(self):
        self.__multimedias=[]
    
    
    def size(self):
        return len(self.__multimedias)
    
    def add(self,m):
        if len(self.__multimedias)==self.__MAX:
            return False
        else:
            self.__multimedias.append(m)
            return True
    
    def get(self,posicion):
        return self.__multimedias[posicion]
    
    def toString(self):
        resultado=""
        for multimedia in self.__multimedias:
            resultado=resultado+multimedia.toString()+"\n"
        return resultado