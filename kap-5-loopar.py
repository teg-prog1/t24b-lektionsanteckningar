# for-loopar
# range (kolla på w3schools)

for i in range(7):
    print(i)

namn = "Felicia"

for bokstav in namn:
    print(bokstav)


# while-loopar
# avbryta oändliga loopar (tryck ctrl C)

programmet_kör = True

#while programmet_kör:
    #print("Hej!")

# allt som går att göra med for-loop går att göra med while-loop, men inte tvärtom
start_tal = 0
while start_tal < 7:
    print(start_tal)
    start_tal += 1

print("Klart!")


# while-loop som "spelloop"
rätt_namn = "Therese"
svar = input("Skriv ett namn: ")

while svar != rätt_namn:
    svar = input("Skriv ett namn: ")

# break, kan stoppa en loop
start_tal_2 = 9
while True:
    print(start_tal_2)
    start_tal_2 += 1
    if start_tal_2 == 11:
        break


# nästlade loopar
kör = True
while kör:
    for i in range(8):
        print(i)
    svar = input("Skriv något tal: ")
    if svar == "3":
        kör = False

# Importera random
import random

# Slumpa heltal

slumptal = random.randint(1,7)
print(slumptal)