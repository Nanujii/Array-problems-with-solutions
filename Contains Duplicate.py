#Contains Duplicate
#page 137
class new:
    def dupli(self,L):
        K=[]
        for i in L:
            if i not in K:
                K.append(i)
        if len(K)==len(L):
            print("False")
        else:
            print("True")
                

L=[1,2,3,4,5]
new1=new()
new1.dupli(L)
