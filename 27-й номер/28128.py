f = open("C://28128A.txt")
a = [int(i) for i in f]
a.sort()
a.reverse()
ok = 0
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if (a[i]+a[j])%3 == 0:
            print(a[i]+a[j])
            ok = 1
            break
    if ok == 1:
        break
f = open("C://28128B.txt")
a = [int(i) for i in f]
a.sort()
a.reverse()
ok = 0
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if (a[i]+a[j])%3 == 0:
            print(a[i]+a[j])
            ok = 1
            break
    if ok == 1:
        break