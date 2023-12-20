#Reverse Vowels of a String
def reverse_vowels(s):
  vow=[]
  L=["a","e","i","o","u"]
  M=""
  for i in s:
      if i in L:
          vow.append(i)
  for j in s:
      if j in L:
          M=M+vow.pop()
      else:
          M=M+j
  return M


k = "leetcode"
sol=reverse_vowels(k) 
print(sol)
