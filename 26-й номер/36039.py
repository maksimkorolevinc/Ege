f = open("C://36039.txt")
a = [int(i) for i in f]
a.sort()
sum = 0
count = 0
b = 0
for i in range(len(a)):
    if sum + a[i] <= 99990:
        sum += a[i]
        count += 1
        b = a[i]
max = 0
for i in range(len(a)):
    if sum - b + a[i] <= 99990:
        max = a[i]
print(count, max)