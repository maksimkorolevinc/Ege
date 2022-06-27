for i in range(123456789, 223456790):
    c = 0
    max = 0
    for d in range(2, i):
        if i%d == 0:
            c += 1
            if c > 3:
                break
            if max < d:
                max = d
    if c == 3:
        print(i, max)