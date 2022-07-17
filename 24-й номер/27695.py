f = open("C://27695.txt")
all = [str(i) for i in f]
a = list(all[0])
count = 1
max = 0
for i in range(len(a) - 1):
    if a[i] != a[i+1]:
        count += 1
        if count >= max:
            max = count
    else:
        count = 1
print(max)