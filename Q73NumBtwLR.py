c=False
x=int(input())
a,b=map(int,input().split())

for i in range(a+1,b,1):
    
    if(i==x):
        c=True
        break
    else:
         c=False
if(c==True):
    print("yes")
else:
    print("no")
