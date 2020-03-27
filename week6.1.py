x=int(input())
lis=[int(i) for i in input().split(" ")]
sort=sorted(lis)
k=int(input())
pos=lis[k-1]
if pos in sort :  
  ind=sort.index(pos) + 1
  print(ind,end='')