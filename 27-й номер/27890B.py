f = open("C://27890B.txt")
a = [str(i) for i in f]
all = []
for i in range(len(a)):
    b = a[i].split()
    all.append(b)
for i in range(len(all)):
    all[i][0], all[i][1] = int(all[i][0]), int(all[i][1])
raz = []
sum = 0
for i in range(len(all)):
    raz.append(abs(all[i][0] - all[i][1]))
    if all[i][0] > all[i][1]:
        sum += all[i][0]
    else:
        sum += all[i][1]
raz.sort()
if sum%3 != 0:
    print(sum)
for i in range(len(raz)):
    if (sum - raz[i])%3 != 0:
        print(sum - raz[i])
        break