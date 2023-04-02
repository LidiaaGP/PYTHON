class Barco:
    
    def __init__(self,matricula,largo,ancho):
        self.__matricula=matricula
        self.__largo=largo
        self.__ancho=ancho

    def get_matricula(self):
        return self.__matricula


    def get_largo(self):
        return self.__largo


    def get_ancho(self):
        return self.__ancho


    def set_matricula(self, value):
        self.__matricula = value


    def set_largo(self, value):
        self.__largo = value


    def set_ancho(self, value):
        self.__ancho = value

    def precio_dia_alquiler(self):
        return 40
    
    def toString(self):
        return "Matricula: "+self.__matricula+" Largo: "+str(self.__largo)+" Ancho: "+str(self.__ancho)+" Precio alquiler: "+str(self.precio_dia_alquiler())
    