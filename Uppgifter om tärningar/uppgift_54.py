import random
antal_slag = 10000
antal_sidor = 5
antal_tärningar = 2

frekvenslista = [0 for _ in range(antal_tärningar, antal_sidor*antal_tärningar+1)]

for slag in range(antal_slag):
    resultat_slag = [random.randint(1,antal_sidor) for _ in range(antal_tärningar)]
    summa_slag = sum(resultat_slag)
    frekvenslista[summa_slag-antal_tärningar]+=1

for index in range(antal_tärningar, antal_sidor*antal_tärningar+1):
    print(f"Antal {index}: {frekvenslista[index-antal_tärningar]}")

