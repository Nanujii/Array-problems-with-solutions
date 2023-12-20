#Minimum in rotated array
L=[4,5,6,7,0,1,2]
L1=[]
L2=[]
for i in range(len(L)):
    if L[i]<L[i+1]:
        continue
    else:
        L1=L[0:i+1]
        L2=L[i+1:]
        break
print(L2[0])
        
