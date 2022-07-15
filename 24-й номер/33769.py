f = open("C://33769.txt")
a = [str(i) for i in f]
all = []
best = []
for i in range(len(a)):
    b = list(a[i])
    for j in range(len(b)):
        all.append(b[j])
for i in range(2, len(all)):
    if all[i-1] == all[i-2]:
        best.append(all[i])
print(best)
max = 0
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alph = list(alph)
for i in range(len(alph)):
    count = 0
    for j in range(len(best)):
        if best[j] == alph[i]:
            count += 1
    if max < count:
        max = count
        print(max, alph[i])