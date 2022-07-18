f = open("C://38602.txt")
all = [str(i) for i in f]
a = list(all[0])
count = 1
max = 0
for i in range(len(a)-1):
    if a[i] + a[i+1] != 'PP':
        count += 1
        if max <= count:
            max = count
    else:
        count = 1
print(max)