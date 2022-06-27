max = 0
for i in range(120115, 120201):
    c = 0
    for d in range(1, i+1):
        if i%d == 0:
            c += 1
    if max < c:
        max = c
        print(max, i)