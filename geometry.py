#This file contains work on Euclidean geometry (e.g. angles, etc.)

import math

def degrees_to_radians(degrees,radians):
    output=2 * math.pi/(360/degrees)
    return output

def radians_to_degrees(radians,degrees):
    output=360/(2 * math.pi/radians)
    return output

def opt_VtoSA_cube(V):
    output=6*(V**(1/3))**2
    return output

def opt_VtoSA_cylinder(V):
    output=((V/math.pi)/2)**(1/2)
    return output

def opt_SAtoV_cube(SA):
    output=((SA/6)**(1/2))**3
    return output

def opt_SAtoV_cylinder(SA):
    output=(((SA/(6*math.pi))**1/2)**3)*2*math.pi
    return output
