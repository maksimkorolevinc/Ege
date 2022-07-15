f = open("C://26.1.txt")
a = [int(i) for i in f]
s = 0
c = 0
b = []
while s < 8358:
    min = 101
    for j in range(len(a)):
        if a[j] < min:
            min = a[j]
    b.append(min)
    for l in range(a.count(min)):
        s += min
        if s > 8358:
            break
        c += 1
    for g in range(a.count(min)):
        a.remove(min)
max = 0
for i in range(len(b)):
    if max < b[i]:
        max = b[i]
print(s)
print(max)
print(c)
