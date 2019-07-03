x=int(input())
#print(x)
rem=0
cu=x
while cu!=0:
    di=cu%10
    rem=rem*10+di
    cu=cu//10
    
if(rem==x):
    print("yes")
else:
    print("no")
