f = open("C://37161.txt")
a = [str(i) for i in f]
all = []
for i in range(len(a)):
    b = a[i].split()
    b[0],b[1] = int(b[0]),int(b[1])
    all.append(b)
all.sort()
min = 10001
max = 0
minm = 0
for i in range(len(all) - 1):
    if a[i][0] == a[i+1][0]:
        if a[i][1] + 3 == a[i+1][1]:
            if a[i][0] + 1 > max:
                max = a[i][0]

print(all)
