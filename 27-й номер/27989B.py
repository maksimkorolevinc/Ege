f = open("C://27989B.txt")
a = [int(i) for i in f]
count = 0
for i in range(len(a) - 1):
    for j in range(i+1, len(a)):
        if (a[j]*a[i])%26 == 0:
            count += 1
print(count)