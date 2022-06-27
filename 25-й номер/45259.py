a = "12345"
b = "7"
c = "8"
for i in range(10):
    i = str(i)
    for j in range(10):
        j = str(j)
        n = a + i + b + j + c
        n = int(n)
        if n%23 == 0:
            print(n, n/23)
