f = open("C://27699.txt")
all = [str(i) for i in f]
a = list(all[0])
count = 2
max = 0
for i in range(len(a) - 2):
    if (a[i] + a[i+1] + a[i+2]) == "LDR" or (a[i] + a[i+1] + a[i+2]) == "DRL" or (a[i] + a[i+1] + a[i+2]) == "RLD":
        count += 1
        if count >= max:
            max = count
    else:
        count = 2
print(max)
