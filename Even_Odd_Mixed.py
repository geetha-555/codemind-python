n=int(input())
c=d=0
while n>0:
    r=n%10
    if r%2==0:
        c+=1
    else:
        d+=1
    n=n//10
if c>0 and d==0:
    print("Even")
elif d>0 and c==0:
    print("Odd")
else:
    print("Mixed")
    