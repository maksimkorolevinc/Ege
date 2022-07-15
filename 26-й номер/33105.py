f = open("C://33105.txt")
a = [int(i) for i in f]
a.sort()
sum = 0
b = []
for i in range(len(a)):
    if a[i] <= 100:
        sum += a[i]
    else:
        b.append(a[i])
b.sort()
max = 0
for i in range(len(b)//2):
    sum += b[i] * 0.7
    max = b[i]
for i in range(len(b)//2, len(b)):
    sum += b[i]
print(b)
print(sum)
print(max)