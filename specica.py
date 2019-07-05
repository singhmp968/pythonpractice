x=str(input())
c=0
for i in x:
    if i.isdigit()==False and i.isalpha()==False:
        c=c+1
print(c)
