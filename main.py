def getSmallest(l,x):
  a=[]
  for m in l:
    if m<x:
      a.append(m)
  return a

l=[100,20,40,60,80,200]
x=60
print(getSmallest(l,x))