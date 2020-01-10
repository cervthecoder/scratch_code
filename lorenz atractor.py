from turtle import *

x = 1
y = 1
z = 1
r = 0
while True:
    if r == 1:
        r += 0.0001
        x = 10 * (y-x)
        y = x * (r-z) - y
        z = x*y - (8/3)*z
    else:
        r += -0.0001
        x = 10 * (y-x)
        y = x * (r-z) - y
        z = x*y - (8/3)*z

    print(x, "\n", y, "\n", z)
    
