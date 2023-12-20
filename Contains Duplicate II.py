#Contains Duplicate II
L=[1,2,3,1]
T=3
H=0
for i in range(len(L)):
    for j in range(i+1,len(L)):
        if L[i]==L[j]:
            if (j-i)<=T:
                print("True")
                H=1
                break
if H!=1:
    print("False")
     
    
