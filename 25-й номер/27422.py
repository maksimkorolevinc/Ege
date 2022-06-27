print("NUMBER 27422")

for i in range(174457, 174506):
    n = i
    c = 0
    for d in range(2, n):
        if n%d == 0:
            c += 1
    if c == 2:
        for j in range(2, n):
            if n%j == 0:
                print(j)
        print("_____")
