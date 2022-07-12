def ishappy(N):
    num=s=0
    
    while(N>0):
        num = N%10
        s+=num**2
        N//=10
    return s

N=int(input())
ans=N

while (ans!=1 and ans!=4):
    ans = ishappy(ans)

if(ans==1):
    print(N,"is happy number")
elif(ans==4):
    print(N,"is not a happy number")
