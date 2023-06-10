n=int(input())
l=list(map(int,input().split()))
s=0
m=0
for i in range(n):
    if(l[i]%2==0):
        s=s+l[i]
    else:
        m=m+l[i]
print(abs(s-m))