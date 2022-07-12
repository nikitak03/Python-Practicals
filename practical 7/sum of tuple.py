from sys import stdin, stdout, setrecursionlimit
def intuple(): return tuple(map(int, stdin.readline().strip().split()))
t=intuple()
s=0
for i in t:
    s+=i
print("The sum of tuple elements is",s)
