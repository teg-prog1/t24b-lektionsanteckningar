import random
antal_slag = 10000
antal_sidor = 6

frekvenslista = [0 for _ in range(antal_sidor)]

for slag in range(antal_slag):
    tärning = random.randint(1,antal_sidor)
    frekvenslista[tärning-1]+=1

for index in range(antal_sidor):
    print(f"Antal {index+1}: {frekvenslista[index]}")

