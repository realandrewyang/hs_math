import math

def twopoints(x1,y1,x2,y2):
    m=(y2-y1)/(x2-x1)
    b=y1-m*x1
    return 'y='+str(m)+'x+'+str(b)

def twointercepts(x_int,y_int):
    m=(y_int-0)/(0-x_int)
    b=y_int
    return 'y='+str(m)+'x+'+str(b)

def slopepoint(m,x,y):
    b=y-m*x
    return 'y='+str(m)+'x+'+str(b)

#Converts an equation from standard form to slope-intercept form
def slopeintercept(A,B,C):
    #Initializes variables
    m=0.0
    b=0.0
    #Sorts through the postive/negative of A,B and C
    if B<0:
        A=-A
        B=-B
        C=-C
    A=-A
    C=-C
    #Solves for m and b
    m=A/B
    b=C/B
    return 'y='+str(m)+'x+'+str(b)

#Converts an equation from slope-intercept from to standard form
def standardform(m,b):
    #Initializes variables
    sign1=''
    sign2=''
    A=-m
    B=1
    C=-b
    #i is the LCM that is being tested to turn A,B, and C into integers
    i=0.0000000000000000000000000000000000000000000000000000000001

    while A!=int(A) and B!=int(B) and C!=int(C):
        A=A*i
        B=B*i
        C=C*i
        i=i+0.0000000000000000000000000000000000000000000000000000000001

    A=int(A)
    B=int(B)
    C=int(C)

    #Ensures that A is positive and clears up some formatting issues
    if A<0:
        A=-A
        B=-B
        C=-C
    if B>0:
        sign1='+'
    if C>0:
        sign2='+'

    return str(A)+'x'+sign1+str(B)+'y'+sign2+str(C)+'=0'

#Switches the equation of a line from one form to the other
def convertequation(equation):
    if equation[0]=='y':
        #Finds two reference points to obtain m and b
        reference1=equation.find('=')+1
        reference2=equation.find('x')
        m=float(equation[reference1:reference2])
        b=float(equation[reference2+2:-1])
        return standardform(m,b)

    else:
        #Finds A,B and C
        A=float(equation[0:equation.find('x')])
        B=float(equation[equation.find('x')+1:equation.find('y')])
        C=float(equation[equation.find('y')+1:equation.find('=')])
        return slopeintercept(A,B,C)   

        
