# Python program to solve quadratic equation
import math
print("Quadratic equation is of the form ax^2 + bx + c =0\n enter the values of a,b,c")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
D=(math.pow(b,2)-(4*a*c))
if(D<0):
    print("Roots of the quadratic equation",a,"x^2 +",b,"x +",c,"are img",sep="")
    exit()
b*=-1
root1=(b+D)/(2*a)
root2=(b-D)/(2*a)
print("Roots of the quadratic equation",a,"x^2 +",b,"x +",c,"are",root1,"and",root2,sep="")
