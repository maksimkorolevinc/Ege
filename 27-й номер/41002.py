f = open("C://41002.txt")
a = [int(i) for i in f]
a.remove(a[0])
left, right = [], []
for i in range(1000):
    left.append(2*1000000)
sum = 0
count = 0
maxs = 0
for i in range(len(a)):
    sum += a[i]
    if a[i]%2 != 0 and abs(a[i]) == a[i]:
        count += 1
    d = count%30
    if sum < left[d]: left[d] = sum
    maxs = max(maxs, sum - left[d])
print(maxs)
f = open("C://41002B.txt")
a = [int(i) for i in f]
a.remove(a[0])
left, right = [], []
for i in range(1000):
    left.append(2*1000000)
sum = 0
count = 0
maxs = 0
for i in range(len(a)):
    sum += a[i]
    if a[i]%2 != 0 and abs(a[i]) == a[i]:
        count += 1
    d = count%30
    if sum < left[d]: left[d] = sum
    maxs = max(maxs, sum - left[d])
print(maxs)
