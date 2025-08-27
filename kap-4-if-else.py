# if
# indentering
ålder = int(input("Hur gammal är du? "))
if ålder < 18:
    print("Du är inte myndig")
if ålder > 25:
    print("Du är vuxen på riktigt")

# jämförelser (==,<, >, <=, >=, !=)
if ålder == 18:
    print("Hej")

# else
# elif

if ålder == 18:
    print("Grattis!")
elif ålder < 20:
    print("Hello")
elif ålder == 54:
    print("Goddag")
else:
    print("Hej!")

# Kan man inte ha bara massa if istället för elif?
if ålder == 18:
    print("Grattis!")
if ålder < 20:
    print("Hello")
else:
    print("Hej!")  


# pass
if ålder == 18:
    print("Grattis!")
elif ålder < 20:
    pass
elif ålder == 54:
    print("Goddag")
else:
    print("Hej!")

# booleans
programmet_kör = True
if programmet_kör == True:
    print("Vi har startat!")

if programmet_kör:
    print("Vi har startat!")

# bool == True

# jämförelser blir booleans

# and, or, not (inte xor)
# prioriteringsregler med and/or
vi_är_redo = False
if not vi_är_redo:
    print("Godmorgon")

if vi_är_redo and programmet_kör:
    print("Båda är sanna")

if vi_är_redo or programmet_kör:
    print("Båda är sanna")

är_pigg = True

if (är_pigg or vi_är_redo) and programmet_kör:
    print("Hej!")

ålder_1 = 54
ålder_2 = 38

if 20 == ålder_1 or ålder_2:
    pass

# nästlade if-else, vi kan ha if/elif/else inuti andra if/elif/else

if ålder_2 == 10:
    if ålder_1 < 2:
        pass
    else:
        pass
