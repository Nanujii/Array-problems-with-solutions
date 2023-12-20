L=[3, 1, 2, 4, 5]
L=[1, 5, 4, 3]
max1=0
for i in range(len(L)):
    for j in range(i+1,len(L)):
        width=j-i
        height=min(L[i],L[j])
        
        area=width*height
        max1=max(max1,area)
print(max1)
