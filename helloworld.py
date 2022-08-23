print ("hellou world! UwU <3")

from turtle import *

speed(300)
width(2)

def right_arc(radius, angle):
    for i in range(angle):
        forward(2*3.14*radius/360)
        right(1)

def centered_arc(radius, angle):
    penup()
    left(angle/2)
    forward(radius)
    right(90)
    pendown()
    right_arc(radius, angle)
    penup()
    left(90)
    back(radius)
    left(angle/2)

def centered_arc(radius, angle):
    penup()
    left(angle / 2)
    forward(radius)
    right(90)
    pendown()
    for i in range(angle):
        forward(2 * 3.14 * radius / 360)
        right(1)
    penup()
    left(90)
    back(radius)
    left(angle / 2)
    pendown()


def right_arc(radius, angle):
    for i in range(angle):
        forward(2 * 3.14 * radius / 360)
        right(1)

def eye():
    # white of the eye
    color('black', 'white')
    begin_fill()
    circle(50)
    end_fill()
    forward(25)
    # pupil
    color('black', 'black')
    begin_fill()
    circle(25)
    end_fill()
    back(25)

def circle(radius):
    penup()
    forward(radius)
    pendown()
    left(90)
    begin_fill()
    for i in range(60):
        forward(3.14 * radius / 30)
        left(6)
    end_fill()
    right(90)
    penup()
    back(radius)
    pendown()


color('black','yellow')
circle(300)     #head
penup()
left(90)
forward(100)
left(90)
forward(75)
left(90)
pendown()
eye()           #lefteye
penup()
left(90)
forward(150)
right(100)
pendown()
eye()           #righteye
penup()
right(80)
forward(75)
left(90)
forward(100)
width(15)       #smile alkaa täst
forward(130)
pendown()
left(20)        #crooked smile
color('red')
centered_arc(50, 180)

hideturtle()
done()