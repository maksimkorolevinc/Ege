f = open("C://27689.txt")
all = [str(i) for i in f]
a = list(all[0])
count = 2
max = []
for i in range(len(a)-2):
    if (a[i] == "X" and a[i+1] == "Y" and a[i+2] == "Z") or (a[i] == "Y" and a[i+1] == "Z" and a[i+2] == "X") or (a[i] == "Z" and a[i+1] == "X" and a[i+2] == "Y"):
        count += 1
        max.append(count)
    else:
        count = 2
max.sort()
max.reverse()
print(max[0])