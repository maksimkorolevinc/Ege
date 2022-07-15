f = open("C://27891A.txt")
a = [int(i) for i in f]
max = 0
for i in range(len(a) - 1):
    for j in range(i, len(a)):
        if (a[j]*a[i])%14 == 0 and max < a[j]*a[i]:
            max = a[i]*a[j]
print(max)
print(a)