from turtle import *

pen = Turtle()

x = 1
y = 2
coef_1 = 0.25
coef_2 = 0.5
expo = 0.000000000000000005

while True:
    for i in range(10):
        expo = expo - 0.25
        x = ((x * coef_1 + i) / coef_2)
        y = ((y * coef_2 + i) * coef_1)
        pen.pendown()
        pen.setposition(x, y)

    for _ in range(10):
        expo = expo - 0.25
        x = ((x * coef_2 + _) * coef_1)
        y = ((y * coef_1 + _) / coef_2)
        pen.pendown()
        pen.setposition(x, y)
    for i in range(10):
        expo = expo - 0.25
        x = ((x / coef_1 + i) / coef_2)
        y = ((y * coef_2 + i) * coef_1)
        pen.pendown()
        pen.setposition(x, y)

    for _ in range(10):
        expo = expo - 0.25
        x = ((x / coef_2 + _) * coef_1)
        y = ((y * coef_1 + _) / coef_2)
        pen.pendown()
        pen.setposition(x, y)

