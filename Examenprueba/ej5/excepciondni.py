class excepciondni(Exception):
    def __init__(self):
        self.__mensaje="el dni tiene que tener 9 caracteres"
    def get_mensaje(self):
        return self.__mensaje