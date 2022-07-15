f = open("C://27990A.txt")
a = [int(i) for i in f]
count = 0
for i in range(len(a) - 1):
    for j in range(i+1, len(a)):
        if a[i]*a[j] == 62:
            count += 1
print(count)
f = open("C://27990B.txt")
a = [int(i) for i in f]
count = 0
for i in range(len(a) - 1):
    for j in range(i+1, len(a)):
        if a[i]*a[j] == 62:
            count += 1
print(count)