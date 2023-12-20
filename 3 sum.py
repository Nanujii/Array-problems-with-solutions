#3 Sum
#page 145
L=[-1,0,1,2,-1,-4]
M=[]
L1=[]
for i in range(len(L)-3):
    for j in range(i+1,len(L)):
        for k in range(j+1,len(L)):
            M.append(L[i])
            M.append(L[j])
            M.append(L[k])
            L1.append(M)
            M=[]
print(L1)
for i in L1:
    if sum(i)==0:
        print(i)
