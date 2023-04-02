import datetime

class Encendido_Luces:
    
    
    def __init__(self):
        self.__horaEncendidoA=0
        self.__horaApagadoA=0
        self.__horaEncendidoB=0
        self.__horaApagadoB=0
        self.__franjaHorariaAEstablecida=False
        self.__franjaHorariaBEstablecida=False
    
    def anularFranjaHorariaA(self):
        self.__franjaHorariaAEstablecida=False
    
    def anularFranjaHorariaB(self):
        self.__franjaHorariaBEstablecida=False
    
    def encender(self):
        horaaactual=datetime.datetime.now().hour
        if (self.__franjaHorariaAEstablecida==True and horaaactual>=self.__horaEncendidoA and horaaactual<=self.__horaApagadoA) or (self.__franjaHorariaBEstablecida==True and horaaactual>=self.__horaEncendidoB and horaaactual<=self.__horaApagadoB):
            print("Encender las luces")
        else:
            print("No hay que encender las luces")

    def establecerFranjaHorariaA(self,heA,haA):
        if heA>=8 and haA<=23:
            if (haA>heA):
                if self.__franjaHorariaBEstablecida==True:
                    if haA<self.__horaEncendidoB:
                        self.__horaEncendidoA=heA
                        self.__horaApagadoA=haA
                        self.__franjaHorariaAEstablecida=True
                        print("Franja horaria A establecida de ",heA," a ",haA)
                    else:
                        print("ERROR. Si la franja horaria B ha sido establecida la hora de apagado A debe ser anterior a la hora de encendido B.")
                else:
                    self.__horaEncendidoA=heA
                    self.__horaApagadoA=haA
                    self.__franjaHorariaAEstablecida=True
                    print("Franja horaria A establecida de ",heA," a ",haA)
            else:
                print("ERROR. Una hora de apagado debe ser siempre posterior a la de encendido")
        else:
            print("ERROR. La hora de encendido debe ser posterior o igual a las 8 y la de apagado anterior o igual a las 23")
    
    def establecerFranjaHorariaB(self,heB,haB):
        if heB>=8 and haB<=23:
            if (haB>heB):
                if self.__franjaHorariaAEstablecida==True:
                    if heB>self.__horaApagadoA:
                        self.__horaEncendidoB=heB
                        self.__horaApagadoB=haB
                        self.__franjaHorariaBEstablecida=True
                        print("Franja horaria B establecida de ",heB," a ",haB)
                    else:
                        print("ERROR. La hora de encendido B debe ser posterior a la hora de apagado A")
                else:
                    print("ERROR. La franja horaria B sólo puede establecerse una vez establecida la franjahoraria A.")
            else:
                print("ERROR. Una hora de apagado debe ser siempre posterior a la de encendido")
        else:
            print("ERROR. La hora de encendido debe ser posterior o igual a las 8 y la de apagado anterior o igual a las 23")
        