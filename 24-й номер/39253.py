f = open("C://39253.txt")
all = [str(i) for i in f]
a = list(all[0])
count = 0
max = 0
counta = []
for i in range(len(a)):
    if a[i] != 'D':
        count += 1
    else:
        counta.append(count)
        count = 0
for i in range(len(counta)-1):
    if counta[i] + counta[i+1] + 1 >= max:
        max = counta[i] + counta[i+1] + 1
print(max)