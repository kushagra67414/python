alphabet=[]
for i in range(97,123):
    alphabet.append(chr(i))
s=input()
s=s.lower()
d=set(s)

for i in d:
    if i in alphabet:
        alphabet.remove(i)
if len(alphabet)==0:
  print("YES",end="")
else:
  print("NO",end="")