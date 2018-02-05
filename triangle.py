import math
import pythagorean

def perimeter(x1,y1,x2,y2,x3,y3):
    #Uses pythagorean to obtain the length of each line
    a=pythagorean.legs(abs(y2-y1),abs(x2-x1))
    b=pythagorean.legs(abs(y3-y1),abs(x3-x1))
    c=pythagorean.legs(abs(y3-y2),abs(x3-x2))
    return [a,b,c,a+b+c]

def istriangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False

def sortpoints(x1,y1,x2,y2,x3,y3):
    #Starts to obtain the dimensions of the smallest possible rectangle
    #that would fit around the triangle
    x_max=max(x1,x2,x3)
    y_max=max(y1,y2,y3)
    x_min=min(x1,x2,x3)
    y_min=min(y1,y2,y3)
    return [x_max,y_max,x_min,y_min]

def area(x1,y1,x2,y2,x3,y3):
    #Finds the dimensions of the smallest possible rectangle that would
    #fit around the triangle
    length=sortpoints(x1,y1,x2,y2,x3,y3)[0]-sortpoints(x1,y1,x2,y2,x3,y3)[2]
    width=sortpoints(x1,y1,x2,y2,x3,y3)[1]-sortpoints(x1,y1,x2,y2,x3,y3)[3]
    #Returns the area of the rectangle minus the area of the remaining space
    final=length*width-(abs(y2-y1))*(abs(x2-x1))/2-(abs(y3-y1))*(abs(x3-x1))/2-(abs(y3-y2))*(abs(x3-x2))/2
    return final
