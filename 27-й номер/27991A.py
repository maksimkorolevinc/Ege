f = open("C://27991A.txt")
a = [int(i) for i in f]
a.sort()
a.reverse()
ok = 0
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if ((abs(a[i] - a[j]))%2 == 0) and (a[i]%17 == 0 or a[j]%17 == 0):
            print(a[i], a[j])
            ok += 1
            break
    if ok == 1:
        break