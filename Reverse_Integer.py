import math
x=int(input())
if(x>=0):
    x=str(x)
    x=x[::-1]
    x=int(x)
    print(x)
else:
    a=abs(x)
    x=str(a)
    x=x[::-1]
    x=int(x)
    print(-x)