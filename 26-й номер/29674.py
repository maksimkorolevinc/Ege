f = open("C://29674.txt")
a = [int(i) for i in f]
a.sort()
sum = 0
b = []
for i in range(len(a)):
    if a[i] <= 50:
        sum += a[i]
    else:
        b.append(a[i])
b.sort()
max = 0
for i in range(len(b)//2):
    sum += b[i] * 0.75
    max = b[i]
for i in range(len(b)//2, len(b)):
    sum += b[i]
print(sum)
print(max)