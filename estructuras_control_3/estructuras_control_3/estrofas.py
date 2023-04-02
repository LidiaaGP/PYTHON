numeroVersos=int(input("Numero Versos: "))
if numeroVersos>=2 and numeroVersos<=4:
    print("Poema:")
    verso1=input()
    vocales=0
    i=len(verso1)-1
    asonante1=""
    consonante1=""
    while(vocales<2):
        if (verso1[i]=='a' or verso1[i]=='e' or verso1[i]=='i' or verso1[i]=='o' or verso1[i]=='u'):
            vocales+=1
            asonante1=verso1[i]+asonante1
        consonante1=verso1[i]+consonante1
        i-=1
    verso2=input()
    vocales=0
    i=len(verso2)-1
    asonante2=""
    consonante2=""
    while(vocales<2):
        if (verso2[i]=='a' or verso2[i]=='e' or verso2[i]=='i' or verso2[i]=='o' or verso2[i]=='u'):
            vocales+=1
            asonante2=verso2[i]+asonante2
        consonante2=verso2[i]+consonante2
        i-=1
    if numeroVersos>=3:
        verso3=input()
        vocales=0
        i=len(verso3)-1
        asonante3=""
        consonante3=""
        while(vocales<2):
            if (verso3[i]=='a' or verso3[i]=='e' or verso3[i]=='i' or verso3[i]=='o' or verso3[i]=='u'):
                vocales+=1
                asonante3=verso3[i]+asonante3
            consonante3=verso3[i]+consonante3
            i-=1
    if numeroVersos==4:
        verso4=input()
        vocales=0
        i=len(verso4)-1
        asonante4=""
        consonante4=""
        while(vocales<2):
            if (verso4[i]=='a' or verso4[i]=='e' or verso4[i]=='i' or verso4[i]=='o' or verso4[i]=='u'):
                vocales+=1
                asonante4=verso4[i]+asonante4
            consonante4=verso4[i]+consonante4
            i-=1
    if numeroVersos==2:
        if consonante1==consonante2:
            print("PAREADO")
        else:
            print("DESCONOCIDO")
    elif numeroVersos==3:
        if consonante1==consonante3 and consonante1!=consonante2:
            print("TERCETO")
        else:
            print("DESCONOCIDO")
    else:
        if consonante1==consonante3 and consonante2==consonante3 and consonante3==consonante4:
            print("CUADERNA VIA")
        elif consonante1==consonante4 and consonante2==consonante3:
            print("CUARTETO")
        elif consonante1==consonante3 and consonante2==consonante4:
            print("CUARTETA")
        elif asonante2==asonante4 and consonante3!=consonante4 and asonante3!=asonante4 and asonante1!=asonante2:
            print("SEGUIDILLA")
        else:
            print("DESCONOCIDO")
else:
    print("ERROR. Numero de versos erroneo")