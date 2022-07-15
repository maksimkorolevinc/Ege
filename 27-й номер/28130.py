f = open("C://28130A.txt")
a = [int(i) for i in f]
a.sort()
count = 0
for i in range(len(a) -1):
    for j in range(i+1, len(a)):
        if (a[j]+a[i])%80 == 0:
            if a[i] > 50 or a[j] > 50:
                count += 1
print(count)
f = open("C://28130B.txt")
a = [int(i) for i in f]
a.sort()
count = 0
for i in range(len(a) -1):
    for j in range(i+1, len(a)):
        if (a[j]+a[i])%80 == 0:
            if a[i] > 50 or a[j] > 50:
                count += 1
print(count)