a,b=map(int,input("").split())
for y in range(a,b,1):
    if y>1:
        for x in range(2,y,1):
            if(y%x==0):
                break
        else:
            print(y ,end=' ')
