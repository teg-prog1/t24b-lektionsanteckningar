# Skapa ett program som utifrån en dictionary med namn och intressen ska skriva ut hur många som har ett visst intresse.
# Exempel på dictionary
'''intressen = {
	"Anna": ["Löpning", "Matlagning", "Målning"],
	“Erik": ["Fotboll", "Målning"],
	"Sara": ["Löpning", "Simning", "Fotboll"],
	"Lena": ["Fotboll", "Matlagning"],
	"Karl": ["Löpning", "Fotboll"]
}
'''
# Exempel på output
'''
Löpning: 3
Matlagning: 2
Målning: 2
Fotboll: 4
Simning: 1
'''

# Övriga krav
'''
Funktion för statistik
    Statistiken skall beräknas i en funktion
    Funktionen ska ta in dictionaryn som argument.
    Returvärdet skall vara en ny dictionary med intressen som nycklar och antal personer som har det intresset som värde.
Huvudprogrammet
    Huvudprogrammet ska använda statistikfunktionen för att generera intressestatistiken.
    Huvudprogrammet ska loopa igenom statistiken och skriva ut resultaten i ett format som visas i exemplen ovan.
    Om det inte finns några intressen att visa statistik för, ska programmet skriva ut: "Inga intressen att visa."
    Huvudprogrammet ska ligga i en egen funktion som anropas när programmet körs.
    Inga variabler ska vara globala.

'''
# En lösning som får något ansatspoäng, men är på svag E-nivå
intressen = {
	    "Anna": ["Löpning", "Matlagning", "Målning"],
	    "Erik": ["Fotboll", "Målning"],
	    "Sara": ["Löpning", "Simning", "Fotboll"],
	    "Lena": ["Fotboll", "Matlagning"],
	    "Karl": ["Löpning", "Fotboll"]
    }

räkna_intressen = {} # skapar en dictionary som ska lagra intressen och antal
for element in intressen: # loopar igenom dictionaryn (men egentligen bara nycklarna)
    for intresse in element[1]: # försöker plocka ut själva listan för att loopa igenom den
        räkna_intressen[element[1]] += 1 # försöker öka antalet för ett intresse

print(räkna_intressen) # skriver ut resultatet, men inte på rätt format








# lite högre nivå, mellan E och C ungefär
intressen = {
	    "Anna": ["Löpning", "Matlagning", "Målning"],
	    "Erik": ["Fotboll", "Målning"],
	    "Sara": ["Löpning", "Simning", "Fotboll"],
	    "Lena": ["Fotboll", "Matlagning"],
	    "Karl": ["Löpning", "Fotboll"]
    }

räkna_intressen = {}

for värde in intressen.values(): # loopar igenom alla intresselistor
    if värde not in räkna_intressen: # kollar om hela listan finns i räkna_intressen, inte bara ett intresse
        räkna_intressen[värde] = 1 # lägger 0 om det inte redan finns = bra
    else:
        räkna_intressen[värde] += 1 # adderar 1 om det finns

for intresse_namn, antal in räkna_intressen.items(): # skriver ut på rätt format
    print(f"{intresse_namn}: {antal}")

# ingen funktion


# Lösning på ca C-nivå

def statistik_intressen(dictionary): # skapar rätt funktioner med parameter enligt instruktion
    statistik_dict = {} 
    
    for lista in dictionary.values(): # loopar igenom alla listor
        for intresse in lista: # loopar igenom varje intresse i listorna
            statistik_dict[intresse] += 1 # lägger till 1 varje gång ett intresse kommer, funkar ej första gången
    return statistik_dict 

def main():
    intressen = {
	    "Anna": ["Löpning", "Matlagning", "Målning"],
	    "Erik": ["Fotboll", "Målning"],
	    "Sara": ["Löpning", "Simning", "Fotboll"],
	    "Lena": ["Fotboll", "Matlagning"],
	    "Karl": ["Löpning", "Fotboll"]
    }

    statistik_intressen(intressen) # anropar statistik-funktionen, men tar inte hand om returvärdet
    for intresse_namn, antal in statistik_dict.items(): # loopar igenom par av intresse och antal
        print(f"{intresse_namn}: {antal}") # skriver ut på rätt format

main()

# Nästan fullständig lösning på A-nivå, men har missat en viktig del i instruktionen = tappar poäng => B-nivå ungefär
def statistik_intressen(dictionary): # Funktion som beräknar antalet av de olika intressena.
                                    # Tar in en dictionary med namn som nyckel och en lista med intressen som värde
                                    # Returnerar en dictionary med intresse som nyckel och antal som har intresset som värde
    statistik_dict = {} # dictionaryn som ska returneras
    
    for lista in dictionary.values(): # loopar igenom varje lista med intressen
        for intresse in lista: # loopar igenom varje intresse
            if intresse not in statistik_dict: # lägger till intresset om det inte finns
                statistik_dict[intresse] = 1
            else:
                statistik_dict[intresse] += 1
    return statistik_dict

def main(): # huvudprogrammet
    intressen = {
	    "Anna": ["Löpning", "Matlagning", "Målning"],
	    "Erik": ["Fotboll", "Målning"],
	    "Sara": ["Löpning", "Simning", "Fotboll"],
	    "Lena": ["Fotboll", "Matlagning"],
	    "Karl": ["Löpning", "Fotboll"]
    }

    färdig_statistik = statistik_intressen(intressen) # anropar funktionen som beräknar statistiken

    for intresse_namn, antal in färdig_statistik.items(): # loopar igenom par av intresse och antal
        print(f"{intresse_namn}: {antal}")

main()

# Fullständig lösning på A-nivå
def statistik_intressen(dictionary): # Funktion som beräknar antalet av de olika intressena.
                                    # Tar in en dictionary med namn som nyckel och en lista med intressen som värde
                                    # Returnerar en dictionary med intresse som nyckel och antal som har intresset som värde
    statistik_dict = {} # dictionaryn som ska returneras
    if not dictionary: # om det inte finns intressen
        return None
    
    for lista in dictionary.values(): # loopar igenom varje lista med intressen
        for intresse in lista: # loopar igenom varje intresse
            if intresse not in statistik_dict: # lägger till intresset om det inte finns
                statistik_dict[intresse] = 1
            else:
                statistik_dict[intresse] += 1
    return statistik_dict

def main(): # huvudprogrammet
    intressen = {
	    "Anna": ["Löpning", "Matlagning", "Målning"],
	    "Erik": ["Fotboll", "Målning"],
	    "Sara": ["Löpning", "Simning", "Fotboll"],
	    "Lena": ["Fotboll", "Matlagning"],
	    "Karl": ["Löpning", "Fotboll"]
    }

    färdig_statistik = statistik_intressen(intressen) # anropar funktionen som beräknar statistiken
    if färdig_statistik == None: # om funktionen returnerade None, dvs inga intressen finns
        print("Inga intressen att visa.")
    else:
        for intresse_namn, antal in färdig_statistik.items(): # loopar igenom par av intresse och antal
            print(f"{intresse_namn}: {antal}")

main()
