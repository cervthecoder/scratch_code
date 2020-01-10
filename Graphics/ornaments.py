from turtle import *
import random
pen = Turtle()

x = 120
posx = 0
posy = 0
d = 25

colors = ['red', 'green', 'blue', 'pink', 'purple', 'black']

while True:
    pen.color(colors[random.randint(0, 5)],)
    while round(360/x) <=48 :
        for _ in range(round(360/x)):
            pen.forward(d)
            pen.right(x)
        x = x/2
    x = 120
    pen.setpos(posy, posx)

    while round(360/x) <=48 :
        for _ in range(round(360/x)):
            pen.forward(d)
            pen.right(-x)
        x = x/2
    posy = posy - 0.001
    x = 120

    pen.setpos(posy, posx)
    pen.clear()




