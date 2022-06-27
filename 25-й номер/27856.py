for i in range(95632, 95651):
    c = 0
    a = []
    for d in range(1, i+1):
        if d%2 != 0 and i%d == 0:
            c += 1
            a.append(d)
    if c == 6:
        print(a)