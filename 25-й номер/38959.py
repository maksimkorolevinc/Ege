s = 0
for i in range(200000000, 1000000000000000):
    a = []
    c = 0
    for d in range(2, i//2):
        if i%d == 0:
            a.append(d)
            c += 1
    M = 1
    if c == 5:
        for j in range(5):
            M *= a[j]
        if M > 0 and M < i:
            print(M, i)
            s += 1
            if s == 5:
                break