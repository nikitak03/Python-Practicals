def ishappy(N):
    num=sum=0
    while(N>0):
        num=N%10
        sum+=num**2
        N//=10
    return sum
for i in range(1,101):
    ans=i
    while(ans!=1 and ans!=4):
        ans= ishappy(ans)

    if(ans==1):
        print(i)
