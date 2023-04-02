class ExcepcionEdad(Exception):
   
    def __init__(self):
        self.__mensaje="la edad debe de estar entre 0 y 130"

    def get_mensaje(self):
        return self.__mensaje

    
    
        