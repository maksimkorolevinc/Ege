f = open("C://36881.txt")
a = [int(i) for i in f]
a.sort()
def b(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
            break
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index
print(a)
count = 0
max = 0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        average = 0
        if (a[i]%2 == 0 and a[j]%2 == 0) or (a[i]%2 != 0 and a[j]%2 != 0):
            average = a[i] + a[j]
            if average == a[b(a, average)]:
                count += 1
                if average > max:
                    max = average
                break
print(count, max)
