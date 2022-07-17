f = open("C://27421.txt")
all = [str(i) for i in f]
a = list(all[0])
count = 1
max = []
for i in range(len(a)-1):
    if a[i] != a[i+1]:
        count += 1
        max.append(count)
    else:
        count = 1
max.sort()
max.reverse()
print(a)
print(max[0])