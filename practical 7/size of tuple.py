from sys import stdin, stdout, setrecursionlimit
def intuple(): return tuple(map(int, stdin.readline().strip().split()))

print("Enter the elements of tuple seperated by space: ")
t=intuple()
s=0
for i in t:
    s+=1
print("The size of entered tuple is",s)
