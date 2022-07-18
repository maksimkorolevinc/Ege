f = open("C://36879.txt")
all = [str(i) for i in f]
a = []
for i in range(len(all)):
    b = list(all[i])
    a.append(b)
max = 0
for i in range(len(a)):
    count = 0
    for j in range(len(a[i])):
        if a[i][j] == "G":
            count += 1
    if count < 25 and count != 0:
        for x in range(len(a[i])):
            for y in range(len(a[i])-1, x+1, -1):
                if a[i][x] == a[i][y]:
                    if y - x > max:
                        max = y - x
print(max)