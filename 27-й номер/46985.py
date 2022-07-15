f = open("C://46985.txt")
a = [int(i) for i in f]
a.remove(a[0])
count = 0
k = len(a)
for i in range(len(a)):
    for j in range(i, k):
        for k in range(len(a), j, -1):
            sum = 0
            b = a[j:k]
            for o in range(len(b)):
                sum += b[o]
            if sum%999 == 0:
                count += 1
print(count)