class ExcepcionDNI(Exception):
   
    def __init__(self):
        self.__mensaje="El DNI debe de tener 9 caracteres"

    def get_mensaje(self):
        return self.__mensaje

    
    
        