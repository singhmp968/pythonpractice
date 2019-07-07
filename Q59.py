x=int(input(""))
rem=0
temp=x
count=0
while temp!=0:
    rem=temp%10
    count=count+1
    temp=temp//10

print(count)
