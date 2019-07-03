x=int(input())
temp=x
g=0
while temp!=0:
    rem=temp%10
    g+=pow(rem,3)
    temp=temp//10
if(g==x):
    print("yes")
else:
    print("no")
