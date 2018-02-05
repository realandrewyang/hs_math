#This module contains functions that are useful for operations with vectors

def dotProduct(a,b):
    if len(a)!=len(b):
        return "Error - vectors have a different number of dimensions"
    else:
        output=0
        for i in range(0,len(a)):
            output=output+a[i]*b[i]
    return output

def crossProduct(a,b):
    if len(a)!=len(b):
        return "Error - vectors have a different number of dimensions"
    else:
        output=[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
        return output

def magnitude(vec):
    if len(a)!=len(b):
        return "Error - vectors have a different number of dimensions"
    else:
        for i in range(0,len(vec)):
            vec[i]=vec[i]**2
        output=sum(vec)**(1/2)
        if output==int(output):
            return int(output)
        else:
            return output

def projection(a,b):
    if len(a)!=len(b):
        return "Error - vectors have a different number of dimensions"
    else:
        factor=dotProduct(a,b)/magnitude(b)
        for i in range(0,len(b)):
             b[i]=factor*b[i]
        return b

def lineFromTwoPoints(a,b):
    if len(a)!=len(b):
        return "Error - points have a different number of dimensions"
    else:
        d=[]
        for i in range(0,len(b)):
            d.append(b[i]-a[i])
        outputPoint="("+str(a[0])
        outputDirection="("+str(d[0])
        for j in range(1,len(b)):
            outputPoint=outputPoint+","+str(a[j])
            outputDirection=outputDirection+","+str(d[j])
        outputPoint+=")"
        outputDirection+=")"
        output="l: (x,y,z) = "+outputPoint+" + k"+outputDirection
        return output
