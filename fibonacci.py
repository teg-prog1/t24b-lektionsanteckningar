näst_senaste = 1
senaste = 2
print(näst_senaste)
print(senaste)

for i in range(2,7):
    nuvarande = senaste + näst_senaste
    print(nuvarande)
    näst_senaste = senaste
    senaste = nuvarande
