import random

ettor = 0
tvåor = 0
treor = 0
fyror = 0
femmor = 0
sexor = 0

for kast in range(10000):
    tärning = random.randint(1,6)
    if tärning == 1:
        ettor += 1
    elif tärning == 2:
        tvåor += 1
    elif tärning == 3:
        treor += 1
    elif tärning == 4:
        fyror += 1
    elif tärning == 5:
        femmor += 1
    elif tärning == 6:
        sexor += 1

print(f"Antal 1: {ettor}")
print(f"Antal 2: {tvåor}")
print(f"Antal 3: {treor}")
print(f"Antal 4: {fyror}")
print(f"Antal 5: {femmor}")
print(f"Antal 6: {sexor}")