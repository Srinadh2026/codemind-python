n=int(input())
l=len(str(n))
s=n*n
k=s%10**l
if(k==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
