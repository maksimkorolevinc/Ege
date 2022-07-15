f = open("C://26.txt")
a = [int(i) for i in f]
sum = 0
c = 0
b = 0
a.sort()
for i in range(len(a)):
    if sum + a[i] <= 8200:
        sum += a[i]
        c += 1
        biggest = a[i]
print(c)
print(sum)
print(biggest)
max = 0
for i in range(970):
    if sum - biggest + a[i] <= 8200:
        max = a[i]
print(max)