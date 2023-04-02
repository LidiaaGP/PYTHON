
class Encuesta:

    def __init__(self,pregunta):
        self.__pregunta=pregunta
        self.__votosA=0
        self.__votosB=0

    def get_pregunta(self):
        return self.__pregunta

    def get_votos_a(self):
        return self.__votosA

    def get_votos_b(self):
        return self.__votosB

    def incA(self):
        self.__votosA+=1
    
    def incB(self):
        self.__votosB+=1
    
    def total_votos(self):
        return self.__votosA+self.__votosB
    
    def porcentajeA(self):
        if self.total_votos()==0:
            return 0
        else:
            return (self.__votosA/self.total_votos())*100
    
    def porcentajeB(self):
        if self.total_votos()==0:
            return 0
        else:
            return (self.__votosB/self.total_votos())*100

 
    