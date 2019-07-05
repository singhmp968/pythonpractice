n=int(input())
for i in range(1,11,1):
    if i == n:
        f=1
        break
    else:
        f=0
if(f==1):
    print("yes")
elif(f==0):
    print("no")
