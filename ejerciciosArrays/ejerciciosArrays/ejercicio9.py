letras=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
numerodni=int(input("Dime numero DNI: "))
resto=numerodni%23
letra=letras[resto]
print(numerodni,letra)