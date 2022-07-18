f = open("C://27698.txt")
all = [str(i) for i in f]
a = list(all[0])
count = 0
max = 0
for i in a:
    if i == "R":
        count += 1
        if max <= count:
            max = count
    else:
        count = 0
print(max)