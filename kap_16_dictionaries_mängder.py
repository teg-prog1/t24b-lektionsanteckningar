# LITE OM STRÄNGAR OCH LISTOR

# list()
namn = "Felicia Hultén Maltsson!"
#print(list(namn))

# split()
# https://www.w3schools.com/python/ref_string_split.asp
uppdelat = namn.split("l")
#print(uppdelat)

# join()
# https://www.w3schools.com/python/ref_string_join.asp 
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

#print(x)

# MÄNGDER (Obs: finns inte i boken)
# Oordnade och tillåter inte dubletter
frukter = {"äpple", "kiwi", "banan", "äpple"}
#print(frukter)

märken = {"äpple", "ferrari", "volvo"}

#Skapa en tom mängd
tom_mängd = set()

# Metoder för mängder
# https://www.w3schools.com/python/python_ref_set.asp 

# difference()
resultat = frukter.difference(märken)
#print(resultat)

# intersection()
resultat_2 = märken.intersection(frukter)
#print(resultat_2)

# issubset()
ny_mängd = {"äpple"}
resultat_3 = ny_mängd.issubset(frukter)
#print(resultat_3)

# DICTIONARIES
# Nycklar och värden
# Två nycklar kan inte vara samma
# Nycklarna måste vara oföränderliga
# Dictionaries är föränderliga

exempel_dictionary = {"Felicia":26, "Victor":27, "Kamilla":56, "Maximiliam":17}

# Plocka ut värde
print(exempel_dictionary["Felicia"])

# Lägga till värde
exempel_dictionary["Frida"]=24
print(exempel_dictionary["Frida"])

# Ta bort värde
del exempel_dictionary["Kamilla"]
print(exempel_dictionary)

# En lista som värde
land_info = {"Sverige": ["Stockholm", "10 miljoner"], "Norge":["Oslo", "5 miljoner"]}

# Metoder för dictionaries
# https://www.w3schools.com/python/python_dictionaries_methods.asp 
# keys()
nycklar = exempel_dictionary.keys()
print(nycklar)

# values()
värden = list(exempel_dictionary.values())
print(värden)

# items()
par = exempel_dictionary.items()
print(par)

# Loopa igenom dictionary
# Obs: tidigare var inte dictionaries sorterade, det är de nu
# Dock kan du inte komma åt innehållet med index

# Loopa med for element in
for element in exempel_dictionary:
    print(element)

# Loopa med values() eller keys()
for värde in exempel_dictionary.values():
    print(värde)

# Loopa med items()
for element in exempel_dictionary.items():
    print(element)

for nyckel, värde in exempel_dictionary.items():
    print(nyckel, värde)
