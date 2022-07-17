f = open("C://27687.txt")
all = [str(i) for i in f]
a = list(all[0])
count = 0
max = []
for i in range(len(a)):
    if a[i] == "Y":
        count += 1
        max.append(count)
    else:
        count = 0
max.sort()
max.reverse()
print(max[0])
