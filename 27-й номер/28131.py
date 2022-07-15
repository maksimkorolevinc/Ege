f = open("C://28131A.txt")
a = [int(i) for i in f]
ok = 0
max = 0
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if i < j and a[i]>a[j]:
            if (a[i]+a[j])%120 == 0 and max < a[i]+a[j]:
                max = a[i]+a[j]
                k = a[i]
                n = a[j]
print(k, n, max)
f = open("C://28131B.txt")
a = [int(i) for i in f]
ok = 0
max = 0
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if i < j and a[i]>a[j]:
            if (a[i]+a[j])%120 == 0 and max < a[i]+a[j]:
                max = a[i]+a[j]
                k = a[i]
                n = a[j]
print(k, n)
