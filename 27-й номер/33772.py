f = open("C://33529.txt")
a = [str(i) for i in f]
all = []
for i in range(len(a)):
    b = a[i].split()
    for j in range(len(b)):
        b[j] = int(b[j])
    all.append(b)
dif1 =  200001
dif2 = 200001
dif3 = 200001
dif4 = 200001
count0 = 0
count1 = 0
sum = 0
for i in range(len(all)):
    if all[i][0] > all[i][1]:
        sum += all[i][1]
        if all[i][1]%2 == 0:
            count0 += 1
        else:
            count1 += 1
        if (all[i][0]%2 != all[i][1]%2):
            if(all[i][0] - all[i][1] < dif1) and (all[i][0]%2 != 0):
                dif2 = dif1
                dif1 = all[i][0] - all[i][1]
            elif (all[i][0] - all[i][1] < dif2) and (all[i][0]%2 != 0):
                dif2 = all[i][0] - all[i][1]
            if (all[i][0] - all[i][1] < dif3) and (all[i][0]%2 == 0):
                dif4 = dif3
                dif3 = all[i][0] - all[i][1]
            elif (all[i][0] - all[i][1]) and (all[i][0]%2 == 0):
                dif4 = all[i][0] - all[i][1]
    if all[i][1] > all[i][0]:
        sum += all[i][0]
        if all[i][1]%2 == 0:
            count0 += 1
        else:
            count1 += 1
        if (all[i][0]%2 != all[i][1]%2):
            if(all[i][1] - all[i][0] < dif1) and (all[i][1]%2 != 0):
                dif2 = dif1
                dif1 = all[i][1] - all[i][0]
            elif (all[i][1] - all[i][0] < dif2) and (all[i][1]%2 != 0):
                dif2 = all[i][1] - all[i][0]
            if (all[i][1] - all[i][0] < dif3) and (all[i][1]%2 == 0):
                dif4 = dif3
                dif3 = all[i][1] - all[i][0]
            elif (all[i][1] - all[i][0]) and (all[i][1]%2 == 0):
                dif4 = all[i][1] - all[i][0]
if count0 < count1:
    if sum%2 != 0:
        print(sum)
    elif dif3 <= dif1:
        print(sum + dif3)
    elif(count1 - count0) != 1:
        print(sum + dif1)
    elif (dif1 + dif2) < dif3:
        print(sum + dif1 + dif2 )
    else:
        print(sum + dif3)
else:
    if sum%2 == 0:
        print(sum)
    elif dif1 <= dif3:
        print(sum + dif1)
    elif (count0 - count1) != 1:
        print(sum + dif3)
    elif (dif3 + dif4) < dif1:
        print(sum + dif3 + dif4)
    else:
        print(sum + dif1)
f = open("C://33529B.txt")
a = [str(i) for i in f]
all = []
for i in range(len(a)):
    b = a[i].split()
    for j in range(len(b)):
        b[j] = int(b[j])
    all.append(b)
dif1 =  200001
dif2 = 200001
dif3 = 200001
dif4 = 200001
count0 = 0
count1 = 0
sum = 0
for i in range(len(all)):
    if all[i][0] > all[i][1]:
        sum += all[i][1]
        if all[i][1]%2 == 0:
            count0 += 1
        else:
            count1 += 1
        if (all[i][0]%2 != all[i][1]%2):
            if(all[i][0] - all[i][1] < dif1) and (all[i][0]%2 != 0):
                dif2 = dif1
                dif1 = all[i][0] - all[i][1]
            elif (all[i][0] - all[i][1] < dif2) and (all[i][0]%2 != 0):
                dif2 = all[i][0] - all[i][1]
            if (all[i][0] - all[i][1] < dif3) and (all[i][0]%2 == 0):
                dif4 = dif3
                dif3 = all[i][0] - all[i][1]
            elif (all[i][0] - all[i][1]) and (all[i][0]%2 == 0):
                dif4 = all[i][0] - all[i][1]
    if all[i][1] > all[i][0]:
        sum += all[i][0]
        if all[i][1]%2 == 0:
            count0 += 1
        else:
            count1 += 1
        if (all[i][0]%2 != all[i][1]%2):
            if(all[i][1] - all[i][0] < dif1) and (all[i][1]%2 != 0):
                dif2 = dif1
                dif1 = all[i][1] - all[i][0]
            elif (all[i][1] - all[i][0] < dif2) and (all[i][1]%2 != 0):
                dif2 = all[i][1] - all[i][0]
            if (all[i][1] - all[i][0] < dif3) and (all[i][1]%2 == 0):
                dif4 = dif3
                dif3 = all[i][1] - all[i][0]
            elif (all[i][1] - all[i][0]) and (all[i][1]%2 == 0):
                dif4 = all[i][1] - all[i][0]
if count0 < count1:
    if sum%2 != 0:
        print(sum)
    elif dif3 <= dif1:
        print(sum + dif3)
    elif(count1 - count0) != 1:
        print(sum + dif1)
    elif (dif1 + dif2) < dif3:
        print(sum + dif1 + dif2 )
    else:
        print(sum + dif3)
else:
    if sum%2 == 0:
        print(sum)
    elif dif1 <= dif3:
        print(sum + dif1)
    elif (count0 - count1) != 1:
        print(sum + dif3)
    elif (dif3 + dif4) < dif1:
        print(sum + dif3 + dif4)
    else:
        print(sum + dif1)