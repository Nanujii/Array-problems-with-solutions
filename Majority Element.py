#Majority Element
#page 156

L=[3, 3, 4, 2, 4, 4, 2, 4]
k=[]
for i in L:
    k.append(L.count(i))
k.sort()
if (len(L)/2)<k[-1]:
    print("true")
    for i in L:
        if L.count(i)==k[-1]:
            print(i)
            break
else:
    print("false")
    
