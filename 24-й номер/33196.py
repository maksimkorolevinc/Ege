f = open("C://33196.txt")
all = [str(i) for i in f]
a = list(all[0])
alph = "QWERTYUIOPASDFGHJKLZXCVBNM"
alph = list(alph)
best = []
for i in range(1, len(a)):
    if a[i-1] == 'A':
        best.append(a[i])
max = 0
for i in range(len(alph)):
    countl = 0
    for j in range(len(best)):
        if best[j] == alph[i]:
            countl += 1
    if max <= countl:
        max = countl
        print(max, alph[i])