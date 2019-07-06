x=int(input())
su=0
while x!=0:
    rem=x%10
    su=su+rem
    x=x//10
print(su)
