f = open("C://27882.txt")
a = [int(i) for i in f]
sum = 0
c = 0
b = 0
a.sort()
for i in range(len(a)):
    if sum + a[i] <= 543:
        sum += a[i]
        c += 1
        biggest = a[i]
print(c)
max = 0
for i in range(2358):
    if sum - biggest + a[i] <= 543:
        max = a[i]
print(max)