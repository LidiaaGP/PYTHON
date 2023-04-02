numeroLegionarios=int(input("Numero Legionarios: "))
numeroEscudos=0

while numeroLegionarios>0:
    i=1
    while ((i+1)*(i+1))<numeroLegionarios:
        i=i+1
    if i==1:
        numeroEscudos=numeroEscudos+5
    else:
        numeroEscudos=numeroEscudos+(i-2)*4+8+(i*i)
    numeroLegionarios=numeroLegionarios-(i*i)

print("Numero Escudos:",numeroEscudos)