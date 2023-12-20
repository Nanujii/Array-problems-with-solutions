#Rotate Array
#page 138
class Rotate:
    def rt(self,L,a):
        A=L[a*-1:]
        B=L[0:(len(L)-a)]
        print(A+B)

L=[1,2,3,4,5,6,7]
k=4
R=Rotate()
R.rt(L,k)
