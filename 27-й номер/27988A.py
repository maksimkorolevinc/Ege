f = open("C://27988B.txt")
a = [int(i) for i in f]
a.sort()
a.reverse()
max = 0
for i in range(len(a)-1):
    for j in range(i, len(a) - 1):
        if (a[j]*a[i])%26 == 0:
            print(a[j]*a[i])
            max = 1
            break
    if max == 1:
        break
print(a)