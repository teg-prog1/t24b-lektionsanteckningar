# Finns olika typer av fel som kan uppstå
# tex SyntaxError, ValueError, NameError, TypeError

# Vi kan hantera felen med hjälp av try except

# Exempel beräkna procent
def skriv_ut_resultat(antal_rätt,antal_frågor):
    try:
        procent_rätt = (antal_rätt/antal_frågor)*100
        print(f"Du fick {antal_rätt} rätt och {antal_frågor-antal_rätt} fel av totalt {antal_frågor} frågor.")
        print(f"Det motsvarar {procent_rätt}% rätt.")
    except ZeroDivisionError:
        print("Det fanns inga besvarade frågor")


# Exempel fråga om tal
ej_svarat = True
while ej_svarat:
    try:
        ålder = int(input("Skriv in din ålder: "))
        ej_svarat = False
    except ValueError:
        print("Du måste skriva in ett heltal")

# Exempel fråga om tal inklusive egna gränser
ej_svarat = True
while ej_svarat:
    try:
        ålder = int(input("Skriv in din ålder: "))
        if ålder < 0:
            raise ValueError
        ej_svarat = False
    except ValueError:
        print("Du måste skriva in ett heltal som är större än eller lika med 0")

# Exempel med index, två olika fel!
frukter = ["äpple", "banan", "kiwi"]

while True:
    try:
        index = int(input("Vilken frukt (0–2) vill du ha? "))
        if index < 0:
            print("Skriv in ett tal som är mellan 0-2")
        else:
            print("Du fick:", frukter[index])
            break
    except ValueError:
        print("Fel, du har inte skrivit in ett heltal.")
    except IndexError:
        print("Fel, du har skrivit ett för stort tal")
