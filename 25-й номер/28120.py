for i in range(201455, 201471):
    c = 0
    a = []
    for d in range(1, i+1):
        if i%d == 0:
            c += 1
            a.append(d)
    if c == 4:
        print(a)