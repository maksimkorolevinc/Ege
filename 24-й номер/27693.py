f = open("C://27693.txt")
all = [str(i) for i in f]
a = list(all[0])
count = 0
max = 0
for i in a:
    if i == "C":
        count += 1
        if count >= max:
            max = count
    else:
        count = 0
print(max)