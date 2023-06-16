n=int(input())
l=list(map(int,input().split()))
l.reverse()
s=0
for i in range(n):
    k=(2**i)*l[i]
    s=s+k
print(s)
    