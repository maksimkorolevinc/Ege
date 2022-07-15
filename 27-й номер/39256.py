f = open("C://39256.txt")
a = [int(i) for i in f]
a.remove(a[0])
left, right = [], []
for i in range(10):
    left.append(0)
    right.append(0)
sum = 0
count = 0
max = 0
for i in range(len(a)):
    sum += a[i]
    if a[i]%2 != 0:
        count += 1
    d = count%10
    if left[d] == 0:
        left[d] = sum
    right[d] = sum
if count%10 == 0:
    print(sum)
else:
    for i in range(count%10):
        if right[i] - left[i] > max:
            max = right[i] - left[i]
    if right[0] > max:
        max = right[0]
    print(max)
f = open("C://39256B.txt")
a = [int(i) for i in f]
a.remove(a[0])
left, right = [], []
for i in range(10):
    left.append(0)
    right.append(0)
sum = 0
count = 0
max = 0
for i in range(len(a)):
    sum += a[i]
    if a[i]%2 != 0:
        count += 1
    d = count%10
    if left[d] == 0:
        left[d] = sum
    right[d] = sum
if count%10 == 0:
    print(sum)
else:
    for i in range(count%10):
        if right[i] - left[i] > max:
            max = right[i] - left[i]
    if right[0] > max:
        max = right[0]
    print(max)