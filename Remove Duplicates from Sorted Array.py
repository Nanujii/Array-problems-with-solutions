#Remove Duplicates from Sorted Array
#page 159
L=[1,1,2]
L1=[]
for i in L:
    if i not in L1:
        L1.append(i)
print(len(L1))
