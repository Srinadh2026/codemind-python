n=int(input())
k=n
s=0
while(n>0):
    r=n%10
    s=r+s*10
    n=n//10
print(s)