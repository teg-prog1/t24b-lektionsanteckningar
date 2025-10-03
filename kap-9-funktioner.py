# len() är en funktion

tal_lista = [1,2,3,4,5,6,7]
längd = len(tal_lista)
print(längd)

# int() är en funktion
tal_sträng = "1234"
tal_int = int(tal_sträng)


# En funktion är ett block kod som har ett "namn"

# Exempel: hälsningsfunktion (tar inte in något och returnerar ingenting)

def hälsningsfunktion():
    print("Goddag, hoppas du får en trevlig dag!")

hälsningsfunktion() # här anropar vi funktionen


# Läs om terminologin på s 107-toppen av s 108
# parameter
# argument
# anropa/kalla på funktion
# ”Parameter = parkeringsplatsen, argument = bilen som parkerar där.”

# Exempel: räkna summa (en funktion som har två parametrar)
def skriv_summa(tal_1, tal_2):
    summa = tal_1 + tal_2
    print(f"Summan av {tal_1} och {tal_2} är {summa}")

skriv_summa(3,5)

# Exempel: variabler i funktionen är lokala

def test_funktion(x):
    print(f"x är nu inne i funktionen: {x}")
    x += 5
    print(f"Nu är x inne i funktionen: {x}")

x = 4
print(f"Utanför funktionen är x: {x}")
test_funktion(x)
print(f"Nu utanför funktionen är x: {x}")

# Exempel: en funktion som returnerar något (bara en sak)
def multiplikation(faktor_1, faktor_2):
    produkt = faktor_1 * faktor_2
    return produkt

resultat = multiplikation(8,9)
print(resultat)
print(multiplikation(7,8))

# Hur använder vi returvärdet (jämför med input())
# Måste spara det som returneras i en variabel
namn = input("Vad heter du? ")

# Vad är funktioner bra för?

# Göra samma sak flera gånger (exempel: testa om en input är i rätt spann)
def testa_input(svar, lägsta_tillåtna, högsta_tillåtna):
    if lägsta_tillåtna <= svar <= högsta_tillåtna:
        return True
    else:
        return False


# Strukturera kod (exempel: uppgiften resväska)

def lägg_till_i_resväskan(travelbag):
    sak_att_lägga_till = input("Vad vill du lägga till i din resväska?: ")
    travelbag.append(sak_att_lägga_till)

travelbag = []

while True:
   menyval = input("1. Kolla i resväskan\n2. Lägg sak i resväskan\n3. Ta bort sak i resväskan\n4. Avsluta program\n\n")

   if menyval == "1":
       pass

   elif menyval == "2":
       lägg_till_i_resväskan(travelbag)
       print(travelbag)

   elif menyval == "3":
       pass

   elif menyval == "4":
       break


#####################################################################################################################################
# HÄRIFRÅN BÖRJAR GENOMGÅNGEN MICKE

# Revisit travelbag, hur fungerar det med listor som parameter

## Vi tittade igenom travelbag igen, pratade om listor som
## föränderliga.
## Touchade på globala variabler genom att visa att vi inte
## kan tilldela ett nytt värde till variabeln

# Om strukturen i ett program

## Jag pratade om att funktioner är bra för både
## - återanvändbarhet
## - struktur och läsbarhet (minska kognitiv belastning)

# Ha en main-funktion!

## main är best practice
## (och dessutom mycket användbart när vi lär oss programmera)
##
## Målet är att det inte ska finnas några globala variabler
## eller i alla fall mycket få. Utan globala variabler får vi
## kod med funktioner som inte påverkar sin omgivning utöver
## parametrar och returvärden.
##
## När vi lär oss programmera kan vi försäkra oss genom att vi
## inte använder globala variabler av misstag i våra egna funktioner
## om vi låter huvudprogrammet (och alla variabler det behöver)
## finnas i main()-funktion.

# Kort exempel: miniyatzy

## Vi tittade på strukturen, att dela upp ett spel i delar som anropar
## varandra. Se miniyatzy.py

# Om default-värden på parametrar

# Skickar vi inte med en eller två parametrar i anropet
# till den här funktionen så används default-värdena
# från funktionsdefinitionen.
def kasta_tärningar(antal_tärningar = 5, antal_sidor = 6):
    pass

fem_vanliga_tärningar = kasta_tärningar()

# Om att returnera flera saker från en funktion

# Löser vi en andragradsekvation vill vi returnera två svar
def lös_andragradare(p, q):
    x1 = -p/2+((p/2)**2 - q)**0.5
    x2 = -p/2-((p/2)**2 - q)**0.5
    # Kommatecken gör så att returvärdet blir en tuple
    return x1, x2

# Vi får tillbaka en tuple som vi kan använda rakt av
rötter = lös_andragradare(-5, 6)
print(rötter)

# Eller packa upp.
# Direkt vid anropet om vi vill
rot1, rot2 = lös_andragradare(7, 12)
print(rot1, rot2)

# Om lokala och globala variabler (läs s 112-113)

## Utöver vad vi sagt tidigare på lektionen så gick vi igenom exemplen i boken.
## Läs dem på sidorna ovan.

# Varför vill vi undvika globala variabler och vilka variabler är rimliga att ha globala?

## Det här pratade vi inte riktigt om. Jag nämnde det, men ni reflekterade inte själva.
