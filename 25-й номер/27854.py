for i in range(110203, 110246):
    n = i
    c = 0
    for d in range(2, n+1):
        if n%d == 0:
            if d%2 == 0:
                c += 1
    if c == 4:
        for j in range(2, n+1):
            if n%j == 0 and j%2 == 0:
                print(j)
        print("____")