x1=str(input())
s1=False
s2=False
for i in x1:
    if i.isalpha():
        s1=True
    if i.isdigit():
        s2=True
if(s1 ==True and s2==True):
    print("Yes")
else:
    print("No")
