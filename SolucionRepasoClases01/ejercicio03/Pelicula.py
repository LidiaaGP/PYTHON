class Pelicula:
    
    def __init__(self,titulo,productora,director=None,duracion=None,puntuacion=None):
        self.__titulo=titulo
        self.__productora=productora
        self.__director=director
        self.__duracion=duracion
        self.set_puntuacion(puntuacion)

    def get_productora(self):
        return self.__productora

    def set_productora(self, value):
        self.__productora = value

    def get_puntuacion(self):
        return self.__puntuacion

    def set_puntuacion(self, value):
        if value==None or (value>=0 and value<=10):
            self.__puntuacion = value
        else:
            print("ERROR. La puntuacion debe de estar entre 0 y 10")

    def get_titulo(self):
        return self.__titulo

    def get_director(self):
        return self.__director

    def get_duracion(self):
        return self.__duracion

    def set_titulo(self, value):
        self.__titulo = value


    def set_director(self, value):
        self.__director = value

    def set_duracion(self, value):
        self.__duracion = value

    def ver_datos(self):
        print("PELICULA:")
        print("Titulo:",self.__titulo)
        if self.__director==None:
            print("Director: No tiene")
        else:
            print("Director:",self.__director)
        if self.__duracion==None:
            print("Duracion: No tiene")
        else:
            print("Duracion:",self.__duracion)
        if self.__puntuacion==None:
            print("Puntuacion: No tiene")
        else:
            print("Duracion:",self.__puntuacion)
        self.__productora.ver_datos()
    

        