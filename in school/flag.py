from turtle import *

t = Turtle()
t.speed(0)
t.penup()
t.goto(-150, 75)  

def draw_stripe(color, y):
    t.goto(-100, y)
    t.pendown()
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.forward(300)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()
    t.penup()

def germany():
    draw_stripe("black", 75)
    draw_stripe("red", 25)
    draw_stripe("yellow", -25)

germany()
done()