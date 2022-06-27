for i in range(35000000,40000001):
    c = 0
    for d in range(1, i+1):
        while c <= 5:
            if d%2 != 0:
                if i%d == 0:
                    c += 1
    if c == 5:
        print(i)