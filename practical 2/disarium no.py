N=int(input())
num=N
sum=0
len =len(str(N))

while(N>0):
    num=N%10
    sum+= int(num**len)
    N= N//10
    len-=1
if(sum==num):
    print(num,"is disarium num")
else:
    print(num,"is not disarium num")
