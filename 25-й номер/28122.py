for i in range (489421, 489441):
    c = 0
    a = []
    for d in range(1, i+1):
        if i%d == 0:
            c += 1
            a.append(d)
    if c == 4:
        print(a)