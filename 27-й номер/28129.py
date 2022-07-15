f = open("C://28129A.txt")
a = [int(i) for i in f]
ok = 0
a.sort()
a.reverse()
for i in range(len(a) - 1):
    for j in range(i+1, len(a)):
        if (a[j]%160 != a[i]%160) and (a[i]%7 == 0 or a[j]%7 == 0):
            print(a[j], a[i])
            ok = 1
            break
    if ok == 1:
        break
f = open("C://28129B.txt")
a = [int(i) for i in f]
ok = 0
a.sort()
a.reverse()
for i in range(len(a) - 1):
    for j in range(i+1, len(a)):
        if (a[j]%160 != a[i]%160) and (a[i]%7 == 0 or a[j]%7 == 0):
            print(a[j], a[i])
            ok = 1
            break
    if ok == 1:
        break