a = [4, 5, 8, 14, 11]
a.sort()
a.reverse()
for i in range(len(a) - 2):
    for j in range(i+1, len(a)-1):
        for p in range(j+1, len(a)):
            if (a[i] + a[j] + a[p])%3 == 0:
                print(a[i] + a[j] + a[p])

