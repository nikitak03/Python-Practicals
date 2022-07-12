N= int(input())
n=list(map(int,str(N)))
a=sum(n)
if N%a==0:
    print(N,"is a harshad num")
else:
    print(N,"is not a harshad num")
