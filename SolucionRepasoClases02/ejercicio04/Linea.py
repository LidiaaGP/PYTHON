from ejercicio04.Punto import Punto

class Linea:
    
    def __init__(self,puntoIni=Punto(0,0,"A"),puntoFin=Punto(0,0,"B")):
        self.__puntoIni=puntoIni
        self.__puntoFin=puntoFin

    def get_punto_ini(self):
        return self.__puntoIni

    def get_punto_fin(self):
        return self.__puntoFin

    def set_punto_ini(self, value):
        self.__puntoIni = value

    def set_punto_fin(self, value):
        self.__puntoFin = value
 
    def mueveDerecha(self,cantidad):
        self.__puntoIni.desplaza_x(cantidad)
        self.__puntoFin.desplaza_x(cantidad)
    
    def mueveIzquierda(self,cantidad):
        self.__puntoIni.desplaza_x(-cantidad)
        self.__puntoFin.desplaza_x(-cantidad)
    
    def mueveArriba(self,cantidad):
        self.__puntoIni.desplaza_y(cantidad)
        self.__puntoFin.desplaza_y(cantidad)
    
    def mueveAbajo(self,cantidad):
        self.__puntoIni.desplaza_y(-cantidad)
        self.__puntoFin.desplaza_y(-cantidad)
    
    def verLinea(self):
        print("Linea de puntos:",self.__puntoIni.get_nombre(),"(",self.__puntoIni.get_x(),",",self.__puntoIni.get_y(),") y",self.__puntoFin.get_nombre(),"(",self.__puntoFin.get_x(),",",self.__puntoFin.get_y(),")")
    