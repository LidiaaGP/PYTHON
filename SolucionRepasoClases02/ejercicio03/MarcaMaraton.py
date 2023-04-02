class MarcaMaraton:
    
    def __init__(self,horas=0,minutos=0,segundos=0):
        self.set_horas(horas)
        self.set_minutos(minutos)
        self.set_segundos(segundos)

    def get_horas(self):
        return self.__horas

    def get_minutos(self):
        return self.__minutos

    def get_segundos(self):
        return self.__segundos

    def set_horas(self, value):
        if value>=0:
            self.__horas = value
        else:
            print("ERROR. Las horas no pueden ser negativas")

    def set_minutos(self, value):
        if value>=0:
            self.__minutos = value
        else:
            print("ERROR. Los minutos no pueden ser negativos")
        

    def set_segundos(self, value):
        if value>=0:
            self.__segundos = value
        else:
            print("ERROR. Los segundos no pueden ser negativos")
        
    def aSegundos(self):
        return self.__horas*3600+self.__minutos*60+self.__segundos
    
    def siguiente(self):
        if self.__segundos==59:
            self.__segundos=0
            if self.__minutos==59:
                self.__minutos=0
                self.__horas+=1
            else:
                self.__minutos+=1
        else:
            self.__segundos+=1
  
    def anterior(self):
        if self.__segundos==0:
            self.__segundos=59
            if self.__minutos==0:
                self.__minutos=59
                self.__horas-=1
            else:
                self.__minutos-=1
        else:
            self.__segundos-=1
            
    def igualQue(self,m):
        if self.aSegundos()==m.aSegundos():
            return True
        else:
            return False
            
    def menorQue(self,m):
        if self.aSegundos()<m.aSegundos():
            return True
        else:
            return False
        
    def mayorQue(self,m):
        if self.aSegundos()>m.aSegundos():
            return True
        else:
            return False
            
    def verMarca(self):
        print("Horas:",self.__horas,"Minutos:",self.__minutos,"Segundos:",self.__segundos)    
            