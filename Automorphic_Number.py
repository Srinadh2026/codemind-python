n=int(input())
s=n
k=n*n
l=len(str(n))
r=k%(10**l)
if(s==r):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")