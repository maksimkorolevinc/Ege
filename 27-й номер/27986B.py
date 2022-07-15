f = open("C://27986B.txt")
a = [int(i) for i in f]
a.sort()
a.reverse()
max = 0
for i in range(len(a)-1):
    for j in range(i, len(a)):
        if (a[j]*a[i])%7 == 0 and (a[j]*a[i])%49 != 0:
            print(a[j]*a[i])
            max = 1
            break
    if max == 1:
        break
print(a[j]*a[i])