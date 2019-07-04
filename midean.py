import math
x=int(input())
li =[]
li=list(map(int,input('').split()))
li.sort()
l=len(li)
mid=(l/2)
a=math.floor(mid)
print(li[a])
