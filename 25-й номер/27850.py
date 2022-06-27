id = 0
for i in range(245690, 245757):
    n = i
    id += 1
    c = 0
    for d in range(1, n+1):
        if n%d == 0:
            c += 1
    if c == 2:
        print(id, n)
