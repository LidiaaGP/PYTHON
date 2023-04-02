class ExcepcionDNI(Exception):
    
    def __init__(self):
        self.__mensaje="ERROR DNI"

    def get_mensaje(self):
        return self.__mensaje


        
    