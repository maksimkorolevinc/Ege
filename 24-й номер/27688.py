f = open("C://27688.txt")
all = [str(i) for i in f]
a = list(all[0])
count = 1
max = []
for i in range(len(a)):
    if a[i] == 'Z':
        count += 1
        max.append(count)
    else:
        count = 0
max.sort()
max.reverse()
print(a)
print(max[0])