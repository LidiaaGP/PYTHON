class excepcionedad(Exception):
    def __init__(self):
        self.__mensaje="La edad debe estar entre 1 y 120"
        
    def get_mensaje(self):
        return self.__mensaje
    