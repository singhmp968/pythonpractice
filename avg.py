x=int(input())
li=list(map(int,input("").split()))
su=0
avg=1
for i in range(0,x,1):
    su=su+li[i]
    
avg=su//x
a=int(avg)
print(avg)
