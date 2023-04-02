class Reloj:

    def __init__(self):
        self.marca=""
        self.modelo=""
        self.precio=0
        self.stock=0 
        self.esDigital=False

    def get_marca(self):
        return self.__marca


    def get_modelo(self):
        return self.__modelo


    def get_precio(self):
        return self.__precio


    def get_stock(self):
        return self.__stock


    def get_es_digital(self):
        return self.__esDigital


    def set_marca(self, value):
        self.__marca = value


    def set_modelo(self, value):
        self.__modelo = value


    def set_precio(self, value):
        self.__precio = value


    def set_stock(self, value):
        self.__stock = value


    def set_es_digital(self, value):
        self.__esDigital = value


    
