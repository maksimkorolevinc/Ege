f = open("C://36037.txt")
all = [str(i) for i in f]
a = list(all[0])
count = 3
max = 0
for i in range(len(a)-3):
    if (a[i] + a[i+1] + a[i+2] + a[i+3] != "XZZY"):
        count += 1
        if max <= count :
            max = count
    else:
        count = 3
print(max)