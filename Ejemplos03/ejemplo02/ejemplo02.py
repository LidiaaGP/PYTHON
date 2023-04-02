#Diccionarios

agendatelefonos={"pepito":666555444,"Fulanito":444555666}

print(type(agendatelefonos))
print(agendatelefonos)
print(agendatelefonos["pepito"])

nombres=agendatelefonos.keys()
print(type(nombres))
print(nombres)

for nombre in nombres:
    print(nombre,agendatelefonos[nombre])