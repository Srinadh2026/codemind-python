a,b=map(int,input().split())
k=10**b
n1=a%k
l1=len(str(a))
n=10**(l1-b)
n2=a//n
print(abs(n1-n2))
