n=int(input())
n1=int(input())
s=0
m=0
for i in range(1,n+1):
    if(n%i==0):
        s=s+i
    else:
        i+=1
for j in range(1,n1+1):
    if(n1%j==0):
        m=m+j
    else:
        j+=1
if(s==m):
    print("Amicable")
else:
    print("Not Amicable")