SEGUNDOSENUNCIADO=500000
diascompletos=SEGUNDOSENUNCIADO//(24*60*60)
segundosdiaincompleto=SEGUNDOSENUNCIADO%(24*60*60)
horascompletas=segundosdiaincompleto//(60*60)
segundoshoraincompleta=segundosdiaincompleto%(60*60)
minutoscompletos=segundoshoraincompleta//60
segundosminutosincompleto=segundoshoraincompleta%60
print(SEGUNDOSENUNCIADO,"segundos=",diascompletos,"dias",horascompletas,"horas",minutoscompletos,"minutos",segundosminutosincompleto,"segundos")