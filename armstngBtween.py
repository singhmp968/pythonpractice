a,b=map(int,input(' ').split())
for x in range(a,b,1):
    temp=x
    ag=0
    while temp!=0:
        rem=temp%10
        ag+=pow(rem,3)
        temp=temp//10
    if(x==ag):
        print(x,end=' ')
