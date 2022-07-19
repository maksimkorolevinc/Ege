f = open("C://46982.txt")
a = [str(i) for i in f]
a = list(a[0])
count = 0
l = []
all = []
ok = False
for i in range(len(a)):
    if a[i] != 'E':
        l.append(a[i])
    else:
        all.append(l)
        l = []
for i in range(len(all)):
    ok = True
    countf = 0
    for j in range(len(all[i])):
        if all[i][j] == 'F':
            ok = False
    if ok and len(all[i]) >= 10:
        count += 1
print(count)