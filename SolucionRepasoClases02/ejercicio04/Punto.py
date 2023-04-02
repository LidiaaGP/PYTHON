class Punto:
    
    def __init__(self,x,y,nombre=""):
        self.__x=x
        self.__y=y
        self.__nombre=nombre

    def get_x(self):
        return self.__x


    def get_y(self):
        return self.__y


    def get_nombre(self):
        return self.__nombre


    def set_nombre(self, value):
        self.__nombre = value
        
    def desplaza_x(self,cantidad):
        self.__x=self.__x+cantidad
    
    def desplaza_y(self,cantidad):
        self.__y=self.__y+cantidad
        
    def ver_punto(self):
        print(self.__nombre,"(",self.__x,",",self.__y,")")


    
        
    
        