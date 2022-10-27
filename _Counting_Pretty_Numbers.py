t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    s=0
    for j in range(a,b+1):
        rem=j%10
        if(rem==2 or rem==3 or rem==9):
            s+=1
    print(s)