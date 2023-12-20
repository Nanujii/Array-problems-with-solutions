#page 133
#2 Sum II
L=[2,7,11,15]
T=18
sub1=[]
sub=[]
for i in L:
    for j in L:
        if i==j:
            continue
        elif (i+j)==T:
            sub1.append(L.index(i))
            sub1.append(L.index(j))
            break
for i in sub1:
    if i not in sub:
        sub.append(i)
for i in range(len(sub)):
    print("index",i+1,"=",sub[i]+1)
