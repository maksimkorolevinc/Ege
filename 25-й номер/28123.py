for i in range(125256, 125331):
    c = 0
    a = []
    for d in range(2, i+1):
        if d%2 == 0 and i%d == 0:
            c += 1
            a.append(d)
    if c == 6:
        print(a)