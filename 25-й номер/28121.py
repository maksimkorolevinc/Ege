id = 0
for i in range(2422000, 2422081):
    c = 0
    a = []
    id += 1
    for d in range(1, i+1):
        if i%d == 0:
            c += 1
    if c == 2:
        print(id, i)