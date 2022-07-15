f = open("C://33199A.txt")
a = [str(i) for i in f]
all = []
for i in range(len(a)):
    b = a[i].split()
    for j in range(len(b)):
        b[j] = int(b[j])
    all.append(b)
sumAns = 0
sum2 = 0
sum3 = 0
mind = 200000001
for i in range(len(all)):
    max = 0
    min = 1000000000
    mid = 0
    for j in range(3):
        if all[i][j] > max:
            max = all[i][j]
    for j in range(3):
        if all[i][j] < min:
            min = all[i][j]
    mid = all[i][0] + all[i][1] + all[i][2] - max - min
    sumAns += max
    sum2 += mid
    sum3 += min
    if (abs(max - mid)%2 != 0) and (abs(max - mid) < mind):
        mind = abs(max - mid)
    elif (abs(max - min)%2 != 0) and (abs(max - min) < mind):
        mind = abs(max - min)
    elif(abs(min - mid)%2 != 0) and (abs(min - mid) < mind):
        mind = abs(min - mid)
if (sum2 + sum3)%2 != 0:
    print(sumAns)
else:
    print(sumAns - mind)
f = open("C://33199B.txt")
a = [str(i) for i in f]
all = []
for i in range(len(a)):
    b = a[i].split()
    for j in range(len(b)):
        b[j] = int(b[j])
    all.append(b)
sumAns = 0
sum2 = 0
sum3 = 0
mind = 200000001
for i in range(len(all)):
    max = 0
    min = 1000000000
    mid = 0
    for j in range(3):
        if all[i][j] > max:
            max = all[i][j]
    for j in range(3):
        if all[i][j] < min:
            min = all[i][j]
    mid = all[i][0] + all[i][1] + all[i][2] - max - min
    sumAns += max
    sum2 += mid
    sum3 += min
    if (abs(max - mid)%2 != 0) and (abs(max - mid) < mind):
        mind = abs(max - mid)
    elif (abs(max - min)%2 != 0) and (abs(max - min) < mind):
        mind = abs(max - min)
    elif(abs(min - mid)%2 != 0) and (abs(min - mid) < mind):
        mind = abs(min - mid)
if (sum2 + sum3)%2 != 0:
    print(sumAns)
else:
    print(sumAns - mind)
