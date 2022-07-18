f = open("C://35482.txt")
all = [str(i) for i in f]
a = []
for i in range(len(all)):
    b = list(all[i])
    a.append(b)
min = 99999999
id = 0
for i in range(len(a)):
    count = 0
    for j in range(len(a[i])):
        if a[i][j] == "G":
            count += 1
    if count <= min and count != 0:
        min = count
ok = 0
for i in range(len(a)):
    count = 0
    for j in range(len(a[i])):
        if a[i][j] == "G":
            count += 1
    if count == min:
        id = i
        break
alph = 'QWERTYUIOPASDFGHJKLZXCVBNM'
alph = list(alph)
max = 0
for i in range(len(alph)):
    count = 0
    for j in range(len(a[id])):
        if a[id][j] == alph[i]:
            count += 1
    if count > max:
        max = count
        print(max, alph[i])