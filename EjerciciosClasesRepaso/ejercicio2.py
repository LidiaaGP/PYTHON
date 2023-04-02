class EncendidoLuces:
    def __init__(self,HoraEncendidoA,HoraApagadoA,HoraEncendidoB,HoraApagadoB,
                 FranjaHorariaAestablecida,FranjaHorariaBestablecida,horaActual)
        self.__HoraEncendidoA=HoraEncendidoA
        self.__HoraApagadoA=HoraApagadoA
        self.__HoraEncendidoB=HoraEncendidoB
        self.__HoraApagadoB=HoraApagadoB
        self.__FranjaHorariaAestablecida=FranjaHorariaAestablecida
        self.__FranjaHorariaBestablecida=FranjaHorariaBestablecida
        self.__horaActual=horaActual
    
    def Encendido_Luces(self):
        self.__FranjaHorariaAestablecida=false
        self.__FranjaHorariaBestablecida=false
    
    def anularFranjaHorariaA(self):
        self.__FranjaHorariaAestablecida=false
    
    def anularFranjaHorariaB(self):
        self.__FranjaHorariaBestablecida=false
    
    def establecerFranjaHorariaA(self):
        if self.__HoraEncendidoA>=8 and self.__HoraApagadoA>=23:
            if self.__HoraApagadoA>self.__HoraEncendidoA:
                if self.__FranjaHorariaBestablecida:
                    if self.__HoraEncendidoA<self.__HoraEncendidoB:
                        self.__FranjaHorariaAestablecida=true
                        print("Franja horaria A establecida de",self.__HoraEncendidoA,"a",self.__HoraApagadoA)
                    else:
                        print ("Error, la hora de apagado de A debe ser anterior a la hora de encendido B")
                else:
                    self.__FranjaHorariaAestablecida=true
                    print("Franja horaria A establecida de",self.__HoraEncendidoA,"a",self.__HoraApagadoA)
            else:
                print("Error. La hora de apagado debe ser posterior a la hora de encendido")
        else:
            print("Las horas de encendido deben estar entre las 8 y las 23")
            
    
    def establecerFranjaHorariaB(self):
        if self.__HoraEncendidoB>=8 and self.__HoraApagadoB>=23:
            if self.__HoraApagadoB>self.__HoraEncendidoB:
                if self.__FranjaHorariaAestablecida:
                    if self.__HoraEncendidoB<self.__HoraApagadoA:
                        self.__FranjaHorariaBestablecida=true
                        print("Franja horaria B establecida de",self.__HoraEncendidoB,"a",self.__HoraApagadoB)
                    else:
                        print ("Error, la hora de apagado de B debe ser anterior a la hora de encendido A")
                else:
                    self.__FranjaHorariaBestablecida=true
                    print("Franja horaria B establecida de",self.__HoraEncendidoB,"a",self.__HoraApagadoB)
            else:
                print("Error. La hora de apagado debe ser posterior a la hora de encendido")
        else:
            print("Las horas de encendido deben estar entre las 8 y las 23")
                    
            
    def encender(self):
        if self.__FranjaHorariaAestablecida and self.__horaActual>=self.__HoraEncendidoA and horaActual<HoraApagadoA:
            return true
        elif self.__FranjaHorariaAestablecida and self.__horaActual>=self.__HoraEncendidoB and horaActual<HoraApagadoB:
            return true
        else: return false

encendido_luces=EncendidoLuces()
encendido_luces.establecerFranjaHorariaA(6,7);
encendido_luces.establecerFranjaHorariaB(16,14);




