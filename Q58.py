a,k=map(int,input("").split())
li=list(map(int ,input("").split()))
f=0
for i in range(0,len(li),1):
    if k == li[i]:
        f=True
        break
    else:
        f=False
if(f):
    print("yes")
else:
    print("no")
# TODO: write code...
