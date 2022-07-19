f = open("C://45258.txt")
a = [str(i) for i in f]
a = list(a[0])
count = 0
max = 0
for i in range(len(a)-1):
    if a[i] + a[i+1] == 'AB' or a[i] + a[i+1] == 'BA' or a[i] + a[i+1] == 'CB' or a[i] + a[i+1] == 'BC':
        count += 1
        if max <= count:
            max = count
    else:
        count = 1
print(max//2)