#Traping water 
L=[3, 0, 2, 0, 4]
M=[]
for i in range(1,len(L)-1):
    left=max(L[:i])
    right=max(L[i+1:])
    K=min(left,right)
    if L[i]<left and L[i]<right:
        M.append(K-L[i])
print(sum(M))
