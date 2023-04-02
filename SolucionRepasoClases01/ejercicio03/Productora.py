class Productora:
    
    def __init__(self,nombre,paginaWeb):
        self.__nombre=nombre
        self.__paginaWeb=paginaWeb

    def get_nombre(self):
        return self.__nombre

    def get_pagina_web(self):
        return self.__paginaWeb

    def set_nombre(self, value):
        self.__nombre = value

    def set_pagina_web(self, value):
        self.__paginaWeb = value

    def ver_datos(self):
        print("PRODUCTORA:")
        print("Nombre:",self.__nombre)
        print("Pagina Web:",self.__paginaWeb)