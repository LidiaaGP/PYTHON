class Matematicas:
    
    #variable de clase
    variable1=20
    
    #Metodo estatico
    @staticmethod
    def km_a_millas(km):
        #print(variable1) daria fallo
        return km/1.5

print(Matematicas.km_a_millas(20))