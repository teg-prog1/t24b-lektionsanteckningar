### UPPSTART OCH MATEMATISKA OPERATIONER ###

# print
print("Hello world!")

# +, -, *, /
print(4+5)
print(7-2)
print(6*9)
print(4/2)

# modulo, %
print(11%3) # ger rest av divisionen 11/3

# heltalsdivision, //
# tar bort decimalerna, avrundar INTE
print(10/3)
print(10//3)
print(2//3)

# upphöjt i, **
print(3**2)

### HELTAL OCH FLYTTAL ###

# heltal = integer (int)
# går snabbare att räkna med
# representeras med binära tal


# flyttal = float
# decimaltal, med punkt eftersom att Python är amerikanskt


# går att blanda heltal och flyttal
print(5+3.4)

# läs s 34-35 i boken

### VARIABLER ###

# Refererar till något i datorns minne, som en låda
# Tilldelar ett värde till variabeln
ålder = 26

# Vill ha beskrivande variabelnamn, till skillnad från matematiken

# Vissa namn är förbjudna
# Får ej börja med siffror, innehålla vissa specialtecken eller vara ett reserverat ord


# Python klarar å, ä och ö

# Håll er till ett språk, engelska eller svenska

# Håll er till en stil, snake_case eller camelCase
ändrad_ålder = 27
ändradÅlder = 27

# Omvandla mellan flyttal och heltal
float_ålder = float(ålder)
print(ålder)
print(float_ålder)

test_float = 9.6
int_av_test_float = int(test_float)
print(test_float)
print(int_av_test_float)

# Ändra värde på variabel (+= osv)
ålder = ålder + 1
print(ålder)
ålder += 1
print(ålder)

### STRÄNGAR ###

# En datatyp
namn = "Felicia"

# Strängar som tal och tal som strängar
antal_husdjur = "2"

# Starkt typat: kan inte blanda datatyper i beräkningar
# Svagt typat: kan blanda datatyper i beräkningar
# Python är starkt typat

#summa = ålder + antal_husdjur #FUNKAR EJ
summa_int = ålder + int(antal_husdjur)
print(summa_int)

# Slå ihop strängar med + (konkatenera) och str()
summa_sträng = str(ålder) + antal_husdjur
print(summa_sträng)
print("Felicia"+"Anna")


### UTSKRIFTER ###

# Skriva ut flera saker på två sätt
print("Felicia "+"är en lärare")
print("Felicia","är en lärare")

# Skriva ut radbrytningar, citattecken och liknande
print("\"\n")

### INMATNINGAR ###

# input()
print("Hej! Vad heter du?")
svar_namn = input()
print("Hej!",svar_namn)

svar_intresse = input("Vad är ditt intresse?")

# Omvandla input till tal
antal_syskon = int(input("Hur många syskon har du?"))
print(antal_syskon+1)

### KOMPLETTERANDE GENOMGÅNG ###

# Python är case-sensitive

# Dynamiskt typat och statiskt typat
# Python är dynamiskt typat
# dvs vi behöver inte sätta en datatyp direkt
ålder = 27

# Jämför med svagt typat och starkt typat

# print med formatering för att skriva ut variabler

print("Du är:",ålder,"år")
print("Du är: "+str(ålder)+" år")
print(f"Du är {ålder} år")