f = open("C://47021.txt")
a = [str(i) for i in f]
a = list(a[0])
count = 0
l = []
all = []
ok = False
for i in range(len(a)):
    if a[i] != 'A':
        l.append(a[i])
    else:
        all.append(l)
        l = []
for i in range(len(all)):
    ok = True
    countf = 0
    for j in range(len(all[i])):
        if all[i][j] == 'B':
            ok = False
    if ok and len(all[i]) >= 8:
        count += 1
print(count)