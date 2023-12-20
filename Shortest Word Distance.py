#Shortest Word Distance
#page 151
import numpy as np
words = ["practice", "makes", "perfect", "coding",
"makes"]
word1 = "makes"
word2 = "coding"
if words.count(word1)==1 and words.count(word2)==1:
    a=words.index(word1)
    b=words.index(word2)
    if a>b:
        print(a-b)
    else:
        print(b-a)
else:
    a=[]
    b=[]
    for i in range(len(words)):
        if words[i]==word1:
            a.append(i)
        if words[i]==word2:
            b.append(i)
        else:
            continue
    A=np.array(a)
    B=np.array(b)
    if len(A)>len(B):
        k=len(A)
    else:
        k=len(B)
    A.resize(k)
    B.resize(k)
    print(min(A)-min(B))
            
    

