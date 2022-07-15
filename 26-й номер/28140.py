num = str(input("num"))
f = open("C://"+num+".txt")
a = [int(i) for i in f]
s = int(input("s"))
n = int(input("n"))
a.sort()
sum = 0
count = 0
b = 0
max = 0
for i in range(n):
    if sum + a[i] <= s:
        sum += a[i]
        count += 1
        b = a[i]
for i in range(n):
    if sum - b + a[i] <= s:
        sum = sum - b + a[i]
        max = a[i]
print(count, max)