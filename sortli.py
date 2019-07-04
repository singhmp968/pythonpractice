x=int(input())
li =[]
li=list(map(int,input('').split()))
li.sort()

for i in range(0,x,1):
  print(li[i],end=' ')
