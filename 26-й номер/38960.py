f = open("C://38960.txt")
a = [str(i) for i in f]
all, ok, left = [], [], []
sum = 0
count = 0
for i in range(len(a)):
    b = a[i].split()
    all.append(b)
all.sort()
for i in range(len(all)):
    if sum + int(all[i][0]) <= 982000:
        sum += int(all[i][0])
        ok.append(all[i])
        if all[i][1] == 'A':
            count += 1
left = all
trash = []
for i in range(len(ok)):
    left.remove(ok[i])
for i in range(len(ok)):
    if left[i][1] == 'B':
        trash.append(left[i])
for i in range(len(trash)):
    left.remove(trash[i])
j = 0
for i in range(len(ok) - 1, -1, -1):
    if ok[i][1] == 'B':
        if sum + int(left[j][0]) - int(ok[i][0]) <= 982000:
            sum = sum + int(left[j][0]) - int(ok[i][0])
            count += 1
            j += 1
print(count, 982000 - sum)