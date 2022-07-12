rint("Enter the list containing keys: ")
key=inlist()
print("Enter the list containing vlaues: ")
val=inlist()
d={}
if len(key)==len(val):
    for i in range(len(key)):
        d[key[i]]=val[i]
else:
    print("Number of keys are not equal to number of values")

print("The dictionary after merging 2 given lists is",d)
