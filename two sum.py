# Two sum
# page 147
L=[2,7,11,15]
T=9
for i in range(len(L)):
    for j in range(i+1,len(L)):
        if L[i]+L[j]==T:
            print(L.index(L[i]),L.index(L[j]))
