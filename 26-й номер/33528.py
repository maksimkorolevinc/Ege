f = open("C://33528.txt")
n = 4000000
a = [str(i) for i in f]
all = []
sum = 0
count = 0
for i in range(len(a)):
    b = a[i].split()
    b[0] = int(b[0])
    all.append(b)
all.sort()

for i in range(len(all)):
    if all[i][2] == 'A':
        for j in range(int(all[i][1])):
            if sum + int(all[i][0]) <= n:
                sum += int(all[i][0])
for i in range(len(all)):
    if all[i][2] == 'B':
        for j in range(int(all[i][1])):
            if sum + int(all[i][0]) <= n:
                sum += int(all[i][0])
                count += 1

print(all)
print(n - sum)
print(count)