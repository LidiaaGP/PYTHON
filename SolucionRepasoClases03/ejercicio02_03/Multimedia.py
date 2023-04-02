class Multimedia:
    
    def __init__(self,titulo,autor,formato,duracion):
        self.__titulo=titulo
        self.__autor=autor
        self.__formato=formato
        self.__duracion=duracion

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_formato(self):
        return self.__formato

    def get_duracion(self):
        return self.__duracion

    def toString(self):
        return self.__titulo+" "+self.__autor+" "+self.__formato+" "+str(self.__duracion)
    
    def equals(self,m):
        if self.__titulo==m.get_titulo() and self.__autor==m.get_autor():
            return True
        else:
            return False
        