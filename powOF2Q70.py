import math
x=int(input())
#y=int(math.sqrt(x))
y=x
count=0
while y>0:
    y=y//2
    count+=1

power=pow(2,count)
print(power)
