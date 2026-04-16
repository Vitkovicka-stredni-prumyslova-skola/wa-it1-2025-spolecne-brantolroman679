import random

cisla = [random.randint(-1, 11) for i in range(10)]
print(*cisla)

print("Max:", max(cisla))

for i in range(8):
    if cisla[i] == cisla[i+1] == cisla[i+2]:
        print("Jsou 3 stejná po sobě")
        break
else:
    print("Nejsou 3 stejná po sobě")