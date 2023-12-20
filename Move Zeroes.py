#Move Zeroes
#page 153


'''L=[0, 1, 0, 3, 0, 12]
L.sort()
M=L.count(0)
#print(L)
for i in range(M):
    L.append(0)
for i in range(3):
    L.remove(0)
    
print(L)'''

L=[0, 1, 0, 45, 0, 12]
for i in range(len(L)):
    if L[i]==0:
        L.append(0)
        L.remove(L[i])
print(L)
