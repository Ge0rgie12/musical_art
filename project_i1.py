from turtle import *

t = Turtle()
t.speed(10)

t.penup()
t.goto(-200,-100)
t.pendown()

side_length = 30
def square(t,side_length, colour):
    t.color(colour)
    t.begin_fill()
    for num in range(4):
        t.forward(side_length)
        t.right(90)
    t.end_fill()
    t.forward(side_length)

colours_list = ["blue","purple","yellow", "green", "red", "coral", "pink"]

y = -100
x= -200
for n in range(5):
    for c in colours_list:
        square(t,side_length, c)
    t.penup()
    y = y + side_length
    x = x + side_length
    t.goto(x, y)
    t.pendown()
done()