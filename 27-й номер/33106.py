f = open("C://33106A.txt")
a = [str(i) for i in f]
all = []
for i in range(len(a)):
    b = a[i].split()
    all.append(b)
for i in range(len(all)):
    all[i][0], all[i][1] = int(all[i][0]), int(all[i][1])
sum = 0
dif = []
for i in range(len(all)):
    if all[i][1] > all[i][0]:
        sum += all[i][0]
    else:
        sum += all[i][1]
    dif.append(abs(all[i][0] - all[i][1]))
dif.sort()
if sum%3 == 0:
        print(sum)
else:
    for i in range(len(dif)):
        if (sum + dif[i])%3 == 0:
            print(sum + dif[i])
            break
f = open("C://33106B.txt")
a = [str(i) for i in f]
all = []
for i in range(len(a)):
    b = a[i].split()
    all.append(b)
for i in range(len(all)):
    all[i][0], all[i][1] = int(all[i][0]), int(all[i][1])
sum = 0
dif = []
for i in range(len(all)):
    if all[i][1] > all[i][0]:
        sum += all[i][0]
    else:
        sum += all[i][1]
    dif.append(abs(all[i][0] - all[i][1]))
dif.sort()
if sum%3 == 0:
        print(sum)
else:
    for i in range(len(dif)):
        if (sum + dif[i])%3 == 0:
            print(sum + dif[i])
            break