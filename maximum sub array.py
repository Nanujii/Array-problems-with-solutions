#Maximum sub array
L=[-2,1,-3,4,-1,2,1,-5,4]
M=0
for i in range(len(L)):
    for j in range(i+1,len(L)):
        if sum(L[i:j])>M:
            M=sum(L[i:j])
            K=i
            k=j
print(L[K:k])
print(M)
        
