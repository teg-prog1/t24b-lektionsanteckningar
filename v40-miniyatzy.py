import random

def kasta_tärningar(antal_tärningar = 5, antal_prickar = 6):
    # _ är en variabel som andra
    # i Python brukar vi namnge variabler vars värden vi inte använder _
    lst = [random.randint(1,antal_prickar) for _ in range(antal_tärningar)]
    return lst

def skriv_ut_poängalternativ(tärningar):
    pass

def spela_omgång():
    # Gör ett tärningsslag
    tärningar = kasta_tärningar()

    # Slå om tärningar (det här gör vi senare)

    # Skriv ut möjliga poäng för kategorier
    skriv_ut_poängalternativ(tärningar)

def main():
    while True:
        spela_omgång()

