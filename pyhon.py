n=int(input())

for x in range(2,n,1):
    if(n%x!=0):
       count=1 
    else:
        count=0
        break
        
if(count==1):
    print("yes")
elif(count==0):
    print("no")

    
