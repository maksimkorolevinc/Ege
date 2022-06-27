for i in range(210235, 210301):
    c = 0
    n = i
    for d in range(2, n):
        if n%d == 0:
            c += 1
    if c == 4:
        for j in range(2, n):
            if n%j == 0:
                print(j)
        print("_______")