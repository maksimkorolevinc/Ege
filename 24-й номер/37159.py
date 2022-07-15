f = open("C://37159.txt")
a = [str(i) for i in f]
a = list(a[0])
count = 0
counts = []
max = 0
for i in range(len(a)-1):
    if a[i]+a[i+1]!= 'ad' and a[i]+a[i+1] != 'da':
        count += 1
        counts.append(count)
    else:
        count = 0
counts.sort()
counts.reverse()
print(counts[0])