f = open("C://33496.txt")
a = [int(i) for i in f]
a.sort()
b = []
sum = 0
count = 0
for i in range(len(a)):
    if a[i] < 220 and a[i] > 210:
        sum += a[i]
        count += 1
        b.append(a[i])
for i in range(len(b)):
    a.remove(b[i])
for i in range(len(a)):
    if sum + a[i] <= 10000:
        sum += a[i]
        count += 1
n = len(a) - 1
for i in range(len(a)//2):
    if sum - a[i] + a[n-i] <= 10000:
        sum = sum - a[i] + a[n-i]
print(count, sum)