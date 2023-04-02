a=int(input("Dime numero 1: "))
b=int(input("Dime numero 2: "))
c=int(input("Dime numero 3: "))
if a<b and a<c:
    print("Menor:",a)
    if b<c:
        print("Medio:",b)
        print("Mayor:",c)
    else:
        print("Medio:",c)
        print("Mayor:",b)
elif b<a and b<c:
    print("Menor:",b)
    if a<c:
        print("Medio:",a)
        print("Mayor:",c)
    else:
        print("Medio:",c)
        print("Mayor:",a)
else:
    print("Menor:",c)
    if a<b:
        print("Medio:",a)
        print("Mayor:",b)
    else:
        print("Medio:",b)
        print("Mayor:",a)
