import math
hrs,min=map(int,input(" ").split())
hrs1,min1=map(int,input(" ").split())
min2=hrs*60+min
min3=hrs1*60+min1
miniute=min3-min2
minute2=abs(miniute)
hrs3=math.floor(minute2/60)
newmin=minute2%60
print(hrs3,newmin)
