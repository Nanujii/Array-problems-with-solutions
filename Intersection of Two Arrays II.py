def inter(num1,num2):
    L=[]
    for i in num1:
        if i in num2:
            L.append(i)
    return(L)

num1 = [2,2]
num2 = [1,2,2,1]
k=inter(num1,num2)
print(k)
