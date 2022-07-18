f = open("C://33526.txt")
all = [str(i) for i in f]
a = list(all[0])
alph = "QWERTYUIOPASDFGHJKLZXCVBNM"
alph = list(alph)
best = []
for i in range(1, len(a)-1):
    if a[i-1] == a[i+1]:
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