n=int(input())
l=list(map(int,input().split()))
mid=n//2
s=0
l1=[]
l2=[]
for i in range(n):
    if mid<=n:
        l1.append(l[i])
    else:
        l2.append(l[i])
s1=sum(l1)
s2=sum(l2)
d=abs(s1-s2)
if(d%4==0):
    print("X")
else:
    print("Y")
    
    