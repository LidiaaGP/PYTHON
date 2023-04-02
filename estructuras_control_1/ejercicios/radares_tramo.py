metros = int(input("Dime los metros recorridos: "))
maximo = int(input("Dime la velocidad maxima: "))
segundos = int(input("Dime los segundos: "))

kilometros=metros/1000
horas=segundos/3600
media=kilometros/horas

if kilometros<0 or horas<0 or media<0:
    print("Error")
elif media<maximo:
    print("Ok")
elif media>maximo and media<(maximo*1.20):
    print("Multa")
else:
    print("Puntos")

