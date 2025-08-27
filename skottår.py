år = int(input("Skriv ett år: "))

if år % 4 == 0:
    if år % 100 == 0:
        if år % 400 == 0:
            print("det är ett skottår") # om året är delbart både med 4, 100 och 400
        else:
            print("det är inte ett skottår") # om året rä delbart med 100, men inte med 400
    else:
        print("det är ett skottår") # om året är delbart med 4 men inte 100
else:
    print("det är inte ett skottår") # om det inte är delbart med 4
##########################################
if år % 400 == 0:
    print("det är ett skottår")
elif år % 4 == 0 and år % 100 != 0:
    print("det är ett skottår")
else:
    print("det är inte ett skottår")
##########################################
if år % 400 == 0 or år % 4 == 0 and år % 100 != 0:
    print("det är ett skottår")
else:
    print("det är inte ett skottår")