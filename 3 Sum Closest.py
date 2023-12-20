#3 Sum Closest
#page 142
L=[-1,2,1,-1]
T=3
L1=[]
sum1=[]
M=[]
lp=[]
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
    sum1.append(sum(i))
sum1.sort()
for i in sum1:
    if i>0 :
        K=i
        break

for i in L1:
    if sum(i)==K:
        print(i)
        print(sum(i))
        break
    
