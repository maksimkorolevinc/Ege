f = open("C://40740.txt")
a = [str(i) for i in f]
a = list(a[0])
max = 0
c = []
b = []
for i in range(len(a)):
    if a[i] != 'A':
        b.append(a[i])
    if a[i] == 'A':
        c.append(b)
        b = []
for i in range(len(c)):
    count1 = 0
    for x in range(len(c[i])):
        if c[i][x] == 'E':
            count1 += 1
    if count1 > 2:
        if len(c[i]) >= max:
            max = len(c[i])
print(max)