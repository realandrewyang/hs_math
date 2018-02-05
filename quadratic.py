#This module contains functions useful for solving basic problem involving quadratic functions

import math

def process(s):
    a=0
    b=0
    c=0
    s=0
    t=0
    h=0
    k=0
    return None

#For finding x when the quadratic expression is in standard form
def quadratic_formula(a,b,c):
    discriminant=(b**2)-4*a*c
    if discriminant<0:
        return 'No real solutions'
    elif discriminant==0:
        return (0-b)/(2*a)
    else:
        x1=((0-b)+math.sqrt(discriminant))/(2*a)
        x2=((0-b)-math.sqrt(discriminant))/(2*a)
        return [x1,x2]

#For finding the factored form
def factor(a,b,c):
    if int(a)==a and int(b)==b and int(c)==c:
        
    else:
        return 'Invalid: a,b,c must be integers'
