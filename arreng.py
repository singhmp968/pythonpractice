n=int(input())
li=list(map(int,input().split()))
l=len(li)
j=[]
for i in range(0,l,1):
    k=li.index(li[i])
    j.append(k)
    print(li[i],j[i])
