numerodni=int(input("Dime numero DNI: "))
letras="TRWAGMYFPDXBNJZSQVHLCKE"
resto=numerodni%23
letra=letras[resto]
print(numerodni,letra)