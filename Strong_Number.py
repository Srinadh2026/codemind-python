def factorial(r):
    mul=1
    while(r>0):
        mul=mul*r
        r=r-1
    return mul
n=int(input())
t=n
s=0
while(n>0):
    r=n%10
    k=factorial(r)
    s=s+k
    n=n//10
if(s==t):
    print("The number",t,"is a strong number")
else:
    print("The number",t,"is not a strong number")