#Plus One
#page 148
def nanu(S,M):
    L=[]
    for i in S:
        L.append(i)
    if L[0]=="9":
        L.insert(0,"0")
    K=str(int(L[M])+1)
    if len(K)==1:
        L[M]=K
        print(L)
    else:
        L[M]=K[-1]
        M=M-1
        nanu(L,M)
            


H=[]
S="999"
M=-1
nanu(S,M)

[0,0]
