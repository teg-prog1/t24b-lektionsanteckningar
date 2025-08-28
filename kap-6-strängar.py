# OLIKA CITATIONSTECKEN

print("Hej!") # vi kan ha vanliga dubbla citattecken

print('Hej') # vi kan ha enkla (samma tangent som *)

# Vi kan också ha trippla (tre stycken enkla)
# Då kan man ha radbrytningarr och citattecken inuti strängen
print('''Hej, här kan
      jag skriva på två rader och ha "citat" i strängen!''')

# Trippla citattecken kan också användas som kommentarer
'''Det här blir som en kommentar'''

# STRÄNGAR ÄR ITERERBARA
# De är lagrade som en följd av tecken i minnet (se s 76)
namn = "Felicia"
print(namn[0]) # vi börjar räkna från 0, detta kommer att skriva ut första tecknet (F)
print(namn[4]) # detta kommer att skriva ut femte tecknet (c)

# Vi kan loopa igenom en strärng

for bokstav in namn: # för varje bokstav i strängen namn
    print(bokstav)

# Vi kan kolla om bokstäver finns i strängen

if "a" in namn:
    print("Det finns ett a!")

#IMMUTABLE
# Strängar i python är immutable (oföränderliga)
# Det betyder att vi inte kan ändra innehållet på följande sätt
#namn[0] = "G" # gör inte att strängen blir Gelicia istället, istället blir det ett felmeddelande
    
# JÄMFÖRA STRÄNGAR
# Vi kan jämföra strängar precis som tal med == och !=
# == kollar om strängarna är exakt lika
print("Felicia"=="Felicia")
print("FeliciA"=="Felicia")

# != kollar om de är olika
print("Felicia"!="Felicia")
print("FeliciA"!="Felicia")

# BITAR AV STRÄNGAR
# Vi kan ta fram bitar av en sträng (kallas för att slicea (engelska: slice))
hela_namnet = "Felicia Hultén Mattsson"
print(hela_namnet[5:10]) # tar med bokstäverna på plats 5, 6, 7, 8, och 9. Tar inte med på plats 10.
print(hela_namnet[:9]) # tar med bokstäverna på plats 0-8, men inte plats 9 och framåt
print(hela_namnet[4:]) # tar med bokstäverna på plats 4 och framåt, men inte på plats 0, 1, 2 och 3
# Se s 80 för fler exempel

# STRÄNGMETODER
# Vi kan göra massa saker med strängar, det finns en lista på w3Schools över strängmetoder
# https://www.w3schools.com/python/python_strings_methods.asp

# Kolla längden på en sträng
längden = len("potatismos") # ger antalet tecken i strängen
print(längden)

print(len("Hejsan svejsan")) #även mellanslag och andra specialtecken räknas

# räkna förekomsten av en delsträng
test_sträng = "Melissa Mattsson"
antal_dubbel_s = test_sträng.count("ss")
print(antal_dubbel_s)

# göra så att bokstäver är stora/små
print(test_sträng.upper()) # gör alla bokstäver stora
print(test_sträng.lower()) # gör alla bokstäver små

# Finns massa fler metoder, ni får själva testa olika i uppgifterna