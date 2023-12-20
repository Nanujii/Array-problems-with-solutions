#best time to buy and sell stock 2
L=[7, 1, 5, 3, 6, 4]
K=0
M=0
 
for i in range(1,len(L)):
    if L[i]>L[i-1]:
        K=K+(L[i]-L[i-1])
        
        
        
print(K)
