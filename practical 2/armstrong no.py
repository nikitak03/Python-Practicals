N=int(input("enter a no."))
sum=0
temp=N
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if N==sum:
    print(N,"is an armstrong number")
else:
    print(N,"is not an armstrong number")
