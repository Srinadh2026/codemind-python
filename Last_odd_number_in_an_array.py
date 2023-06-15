n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(n):
    if(l[i]%2!=0):
        k.append(l[i])
print(k[-1])