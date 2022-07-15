f = open("C://27986A.txt")
a = [int(i) for i in f]
max = 0
for i in range(len(a)-1):
    for j in range(i, len(a)):
        if (a[j]*a[i])%7 == 0 and (a[j]*a[i])%49 != 0:
            if max < (a[j]*a[i]):
                max = (a[j]*a[i])
print(max)