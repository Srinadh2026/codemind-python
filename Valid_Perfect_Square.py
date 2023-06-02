a=int(input())
for i in range(a):
    import math
    n=int(input())
    s=int(math.sqrt(n))
    if(s*s==n):
        print(True)
    else:
        print(False)
    