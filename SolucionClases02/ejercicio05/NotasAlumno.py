class NotasAlumno:
   
    def __init__(self):
        self.__asignatura=""
        self.__nombre=""
        self.__apellidos=""
        self.__nota_eval1=0
        self.__nota_eval2=0
        self.__nota_eval3=0

    def get_asignatura(self):
        return self.__asignatura


    def get_nombre(self):
        return self.__nombre


    def get_apellidos(self):
        return self.__apellidos


    def get_nota_eval_1(self):
        return self.__nota_eval1


    def get_nota_eval_2(self):
        return self.__nota_eval2


    def get_nota_eval_3(self):
        return self.__nota_eval3


    def set_asignatura(self, value):
        self.__asignatura = value


    def set_nombre(self, value):
        self.__nombre = value


    def set_apellidos(self, value):
        self.__apellidos = value


    def set_nota_eval_1(self, value):
        self.__nota_eval1 = value


    def set_nota_eval_2(self, value):
        self.__nota_eval2 = value


    def set_nota_eval_3(self, value):
        self.__nota_eval3 = value

    def media(self):
        return (self.__nota_eval1+self.__nota_eval2+self.__nota_eval3)/3
    