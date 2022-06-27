for i in range(185311, 185331):
    c = 0
    n = i
    for d in range(1, n + 1):
        if n%d == 0:
            c += 1
    if c == 4:
        for j in range(1, n+1):
            if n%j == 0:
                print(j)
        print("______")