n=int(input())
rev=0
a=n**2
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
sqr=rev**2
re=0
while sqr>0:
    rem=sqr%10
    re=re*10+rem
    sqr=sqr//10
if re==a:
    print("True")
else:
    print("False")
