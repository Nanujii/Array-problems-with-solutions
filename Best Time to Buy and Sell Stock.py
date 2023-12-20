#Best Time to Buy and Sell Stock
#page 150
L=[7,1,5,3,6,4]
k=L[0:]
k.sort()
M=[]
L2=[]
for i in range(len(k)-1,-1,-1):
    M.append(k[i])
if M==L:
    print(0)
else:
    
    mi=min(L)
    L2=L[L.index(mi):]
    ma=max(L2)
    print(ma-mi)
