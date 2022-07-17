f = open("C://27694.txt")
all = [str(i) for i in f]
a = list(all[0])
count = 0
max = 0
for i in range(len(a)-1):
    if (a[i] == "A" and a[i+1] == "B") or (a[i] == "B" and a[i+1] == "A"):
        count += 1
        if count >= max:
            max = count
    else:
        count = 0
print(max)