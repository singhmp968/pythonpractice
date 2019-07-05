def check(x):
    try:
        float(x)
        print("yes")
    except:
        print("No")
x=str(input())
check(x)
