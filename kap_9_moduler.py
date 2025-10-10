# MODULER

# Läs sida 114

# Vi kan kolla vad som finns i en modul

import math
dir(math) # gör så att vi kan använda help

help(math.sqrt) # hjälp med en specifik funktion
# q för att avsluta

help(math) # hjälp med hela modulen

# Kan skapa egna moduler, med funktioner
# Filen måste ligga i samma mapp för att det ska funka på ett enkelt sätt
import test_modul
test_modul.summa(8,9)

