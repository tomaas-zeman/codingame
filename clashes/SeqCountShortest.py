n=input()
x=m=0
for c in n:
 if c=="0":
  x+=1
 else:
  m=max(x,m)
  x=0
print(max(x,m))