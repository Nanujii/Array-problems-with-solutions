#Product of Array Except Self
#page 173
L=[1,2,3,4]
M=[]
for i in range(len(L)):
    k=1
    for j in L:
        if L[i]==j:
            continue
        else:
            k=k*j
    M.append(k)
print(M)
