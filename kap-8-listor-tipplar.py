# fyra datatyper hittills, int, float, bool, string
# string är itererbar
#for bokstav in "Felicia":
    #print(bokstav)

# lista, element
frukt_lista = ["annanas", "päron", 2, 1.3, True]
#print(frukt_lista)

# ordnad
#index
#print(frukt_lista[0])

# går att förändra
#frukt_lista[1] = "banan"
#print(frukt_lista)

# olika datatyper i listor

# loopa igenom lista med for-loop
#for element in frukt_lista:
   # print(element)

# slicea listor
#print(frukt_lista[1:4:2])

# listomfattningar (list comprehensions)
newlist = [tal for tal in range(0,85) if tal%2==0]
#print(newlist)

# Listmetoder ###
# len()
#print(len(frukt_lista))

# append()
frukt_lista.append("kiwi")
#print(frukt_lista)

# min()

# sort() och sorted()

tal_lista1 = [6,8,3,4,5]
print("Lista 1 inte sorterad:")
print(tal_lista1)
tal_lista1.sort()
print("Lista 1 sorterad: ")
print(tal_lista1)

tal_lista2 = [6,8,3,4,5]
print("Lista 2 innan sortering:")
print(tal_lista2)
print("lista 2 efter sortering:")
sorterad_lista_2 = sorted(tal_lista2)
print(sorterad_lista_2)
print("lista 2 igen:")
print(tal_lista2)


# andra metoder på w3shools

# lista med listor, matris
syskon = [["Frida","Maximiliam"],["Pernilla", "August"],["Kent","Karl"]]
print(syskon[0][1])

# tipplar/ tuples
vokaler = ("a","o","u")

# oföränderlig

# ordnad precis som listor

# packa in och packa upp tipplar
vokal_1, vokal_2, vokal_3 = vokaler
print(vokal_1)
print(vokal_2)
print(vokal_3)

ny_vokal_tuple = (vokal_1,vokal_2,vokal_3)
print(ny_vokal_tuple)
#######################################################################################################################
# Läs sida 100-102 "Allting i Python är referenser"

# Referenser i Python

# Skapa ett nytt variabelnamn som refererar till samma lista
# Kopiera en lista

frukt_lista = ["annanas", "banan", "äpple"]

annan_frukt_lista = [frukt for frukt in frukt_lista]
tredje_frukt_lista = frukt_lista[:]

annan_frukt_lista.append("päron")
tredje_frukt_lista.append("papaya")

print(frukt_lista)
print(annan_frukt_lista)
print(tredje_frukt_lista)


# Platser i minnet som inget refereras till längre tas omhand genom Pythons garbage collect





