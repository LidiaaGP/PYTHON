litrosmios=int(input("Dime litros de mi piscina "))
barreñomio=int(input("Dime litros de mi barreño "))
perdidasmias=int(input("Dime litros que pierde mi piscina "))

litrosvecino=int(input("Dime litros de la piscina del vecino "))
barreñovecino=int(input("Dime litros del barreño del vecino "))
perdidasvecino=int(input("Dime litros que pierde la piscina del vecino "))

litrosmipiscina=0
contadormio=0
while(litrosmipiscina<litrosmios and litrosmipiscina>=0):
    litrosmipiscina=litrosmipiscina+barreñomio;
    litrosmipiscina=litrosmipiscina-perdidasmias
    contadormio=contadormio+1

litrospiscinavecino=0
contadorvecino=0
while(litrospiscinavecino<litrosvecino and litrospiscinavecino>=0):
    litrospiscinavecino=litrospiscinavecino+barreñovecino;
    litrospiscinavecino=litrospiscinavecino-perdidasvecino
    contadorvecino=contadorvecino+1
    
if(litrospiscinavecino<0 and litrosmipiscina<0):
    print("Empate 0")
elif(litrospiscinavecino<0):
    print("Gano yo",contadormio)
elif(litrosmipiscina<0):
    print("Gana vecino",contadormio)
elif contadormio>contadorvecino:
    print("Gana vecino ",contadorvecino)
elif contadormio<contadorvecino:
    print("Gano yo ",contadormio)
else:
    print("Empate ",contadormio)