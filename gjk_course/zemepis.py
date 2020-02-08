import math

def gnom(r, angle):
    angle = math.radians(angle)
    return r * math.tan(angle)

def ster(r, angle):
    angle = math.radians(angle/2)
    return 2*r * math.tan(angle)

def ort(r, angle):
    angle = math.radians(angle)
    return r * math.sin(angle)

def lamb(r, angle):
    angle = math.radians(angle/2)
    return 2*r * math.sin(angle)

def post(r, angle):
    return r * 2*math.pi/360 * angle






