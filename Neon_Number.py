n=int(input())
s=0
a=n*n
while a>0:
    r=a%10
    s+=r
    a=a//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")

    
    
    