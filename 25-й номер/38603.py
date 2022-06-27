s = 0
for i in range(700000, 1000000):
    max = 0
    min = i
    a = []
    for d in range(2, i):
        if i%d == 0:
            a.append(d)
    for j in range (len(a)):
        if a[j] < min:
            min = a[j]
        if a[j] > max:
            max = a[j]
    if max != 0 and min != i and (max + min)%10 == 8:
        print(i, min, max, min + max)
        s += 1
        if s == 5:
            break