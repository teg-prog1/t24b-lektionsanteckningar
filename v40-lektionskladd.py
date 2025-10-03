# Strukturera kod (exempel: uppgiften resväska)

# Funktion som används för att göra programmet läsbart
# Gör en sak, används kanske bara från ett ställe, har ett tydligt namn
def lägg_till_i_resväskan(travelbag):
    sak_att_lägga_till = input("Vad vill du lägga till i din resväska?: ")
    travelbag.append(sak_att_lägga_till)

# Använd ALLTID en main-funktion
# Best practice
# Gör det svårare att "programmera fel"
def main():
    travelbag = ["tandborste", "tröja"]

    while True:
        menyval = input("1. Kolla i resväskan\n2. Lägg sak i resväskan\n3. Ta bort sak i resväskan\n4Avsluta program")

        if menyval == "1":
            print(travelbag)

        elif menyval == "2":
            # Tar inte upp mycket skärmutrymme
            # Tydligt vad koden gör
            # Låg kognitiv belastning
            lägg_till_i_resväskan(travelbag)

        elif menyval == "3":
            pass

        elif menyval == "4":
            break
        
main()