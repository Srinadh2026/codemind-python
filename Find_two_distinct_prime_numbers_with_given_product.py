n=int(input())
l=[]
c=0
for i in range(1,n):
    if(n%i==0):
        l.append(i)
for j in range(len(l)):
    for k in range(1,len(l)):
        if(l[j]*l[k]==n):
            print(l[j],l[k],end=" ")
            c=1
            break
    if(c==1):
        break
else:
    print("-1")