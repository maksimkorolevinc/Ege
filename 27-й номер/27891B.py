f = open("C://27891B.txt")
a = [int(i) for i in f]
max = 0
a.sort()
a.reverse()
for i in range(len(a) - 1):
    for j in range(i, len(a)):
        if (a[j]*a[i])%14 == 0:
            print(a[j]*a[i])
            max = 1
            break
    if max == 1:
        break