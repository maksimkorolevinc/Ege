f = open("C://29672.txt")
all = [str(i) for i in f]
a = []
for i in range(len(all)):
    b = list(all[i])
    a.append(b)
count = 0
for i in range(len(a)):
    ec = 0
    ac = 0
    for j in range(len(a[i])):
        if a[i][j] == "E":
            ec += 1
        if a[i][j] == "A":
            ac += 1
    if ec > ac:
        count += 1
print(count)