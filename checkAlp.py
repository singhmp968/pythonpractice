str1 = input()
a1=0
n1=0
for i in str1 :
    if i.isalpha() :
        a1 += 1
    if i.isdigit() :
        n1 += 1
if a1 and n1 : 
    print('Yes')
else : 
    print('No')
