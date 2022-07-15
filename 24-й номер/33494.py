f = open("C://33494.txt")
a = [str(i) for i in f]
a = list(a[0])
alph = 'QWERTYUIOPASDFGHJKLZXCVBNM'
alph = list(alph)
best = []
for i in range(1, len(a)):
    if a[i-1] == 'E':
        best.append(a[i])
max = 0
for i in range(len(alph)):
    count = 0
    for j in range(len(best)):
        if best[j] == alph[i]:
            count += 1
    if max < count:
        max = count
        print(max, alph[i])