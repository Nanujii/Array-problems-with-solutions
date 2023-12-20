#page 135
#2 Sum III
class sum3:
    def add1(self,a):
        L.append(a)
    def find1(self,L,F):
        for i in range(len(L)):
            for j in range(i+1,len(L)):
                M.append(L[i]+L[j])
        if F in M:
            print("TRue")
        else:
            print("False")
                
        
L=[]
M=[]
F=27
K=sum3()
while(True):
    P=int(input("ENter 1 for add 2 for find :"))
    if P==1:
        a=int(input("Enter num :"))
        K.add1(a)
    if P==2:
        a=int(input("Enter num :"))
        K.find1(L,a)
    
    
