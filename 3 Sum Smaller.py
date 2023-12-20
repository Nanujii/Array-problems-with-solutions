
L=[-2,0,1,3]
M=[]
L2=[]
for i in range(len(L)-3):
        for j in range(i+1,len(L)):
            if L[j]>L[i]:
                for k in range(j+1,len(L)):
                    if L[k]>L[j]:
                        M.append(L[i])
                        M.append(L[j])
                        M.append(L[k])                       
                        L2.append(M)
                        M=[]
k=0              
for i in L2:
    if sum(i)<2:
        print(i)
        k=k+1
print(k)                        
 
