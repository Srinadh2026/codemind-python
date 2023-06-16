n=int(input())
l=list(map(int,input().split()))
s=len(l)
c=0
for i in range(n):
    if l[i]==0 or l[i]==1:
        c+=1
if(s==c):
    print(True)
else:
    print(False)