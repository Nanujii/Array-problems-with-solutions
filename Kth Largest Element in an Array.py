#page132
#Kth Largest Element in an Array
class Kth:
    def sol(self,L,k):
        L.sort()
        M=k*-1
        print(L[M])

O=Kth()
L=[3,2,1,5,6,4]
k=2
O.sol(L,k)
