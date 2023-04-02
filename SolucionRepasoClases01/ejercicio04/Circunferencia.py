class Circunferencia:
    
    __PI=3.14159
    
    def __init__(self,radio):
        self.__radio=radio

    def get_pi(self):
        return self.__PI

    def get_radio(self):
        return self.__radio

    def set_pi(self, value):
        if value>=3.14 and value<=3.16:
            self.__PI = value
        else:
            print("ERROR. EL valor de PI debe de estar entre 3.14 y 3.16")

    def set_radio(self, value):
        if value>0:
            self.__radio = value
        else:
            print("ERROR: EL radio debe de ser mayor que 0")

    def area(self):
        return self.__PI*self.__radio*self.__radio
    
    def longitud(self):
        return 2*self.__PI*self.__radio