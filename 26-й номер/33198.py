f = open("C://33198.txt")
a = [int(i) for i in f]
b = []
a.sort()
n = 1000
maximum = 10000
sum = 0
count = 0
for i in range(len(a)):
    if a[i] <= 210 and a[i] >= 200 and sum + a[i] <= maximum:
        sum += a[i]
        count += 1
        b.append(a[i])
for i in range(len(b)):
    a.remove(b[i])
n = len(a) - 1
for i in range(len(a)):
    if sum + a[i] <= maximum:
        sum += a[i]
        count += 1
for i in range(len(a)//2):
    if sum - a[i] + a[n-i] <= maximum:
        sum = sum - a[i] + a[n-i]
print(sum, count)
