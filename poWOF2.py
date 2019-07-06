def getpower(n):
    a=True
    if n==0:
        print(no)
    while n!=1:
        if(n%2!=0):
            a=False
        n=n//2
    if a==False:
        print("no")
    else:
        print("yes")

x=int(input())
getpower(x)
