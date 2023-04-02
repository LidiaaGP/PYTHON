class Encuesta:
    
    def __init__(self, pregunta,votosA,votosB):
        self.__pregunta=pregunta
        self.__votosA=955
        self.__votosB=821
        
    def incA(self):
        return self.__votosA+1
    
    def incB(self):
        return self.__votosB+1
    
    def total_votos(self):
        return self.__votosA+self.__votosB
    
    def porcentajeA(self):
        if encuestafutbol.total_votos()==0:
            return 0
        else:
            return (self.__votosA/encuestafutbol.total_votos())*100
    
    def porcentajeB(self):
        if encuestafutbol.total_votos()==0:
            return 0
        else:
            return (self.__votosB/encuestafutbol.total_votos())*100
    
    def ver_datos(self):
        print("Pregunta:",self.__pregunta)
        print("Total de votos",encuestafutbol.total_votos())
        print("VotosA:",self.__votosA)
        print("VotosB:",self.__votosB)
        print("Porcentaje votosA:",encuestafutbol.porcentajeA(),"%")
        print("Porcentaje votosB:",encuestafutbol.porcentajeB(),"%")
    

encuestafutbol=Encuesta("¿Quién es el mejor jugador de fútbol del mundo, Messi(A) o Cristiano(B)?",0,0)
encuestafutbol.ver_datos()


        