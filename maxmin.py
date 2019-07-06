x=int(input())
li=list(map(int,input("").split()))
max1=li[0]
min1=li[0]
for i in range(1,x,1):
    max1=max(max1,li[i])
    min1=min(min1,li[i])
print(min1,max1)
