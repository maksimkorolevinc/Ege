f = open("C://27985A.txt")
a = [int(i) for i in f]
a.sort()
a.reverse()
max = 0
for i in range(len(a)-1):
    for j in range(i, len(a)):
        if(a[i]*a[j])%14 == 0 and a[i] != a[j]:
            print(a[i]*a[j])
            max = 1
            break
    if max == 1:
        break