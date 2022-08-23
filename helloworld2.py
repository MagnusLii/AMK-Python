from turtle import *

def H():
    left(90)
    forward(100)
    back(50)
    right(90)
    forward(75)
    left(90)
    forward(50)
    back(100)

def spacing():
    penup()
    left(90)
    forward(20)
    pendown()

def E():
    left(90)
    forward(100)
    right(90)
    forward(75)
    back(75)
    right(90)
    forward(50)
    left(90)
    forward(50)
    back(50)
    right(90)
    forward(50)
    left(90)
    forward(75)

def L():
    ### L ###
    left(90)
    forward(100)
    back(100)
    right(90)
    forward(50)

def O():
    forward(50)
    left(45)
    forward(25)
    left(45)
    forward(100)
    left(45)
    forward(25)
    left(45)
    forward(50)
    left(45)
    forward(25)
    left(45)
    forward(100)
    left(45)
    forward(25)

def W():
    left(90)
    penup()
    right(160)
    pendown()
    forward(120)
    left(140)
    forward(80)
    right(140)
    forward(80)
    left(140)
    forward(120)

def R():
    right(45)
    forward(25)
    left(45)
    forward(25)
    left(45)
    forward(25)
    left(45)
    forward(100)

def D():
    left(90)
    forward(100)
    right(90)
    forward(50)
    right(45)
    forward(35)
    right(45)
    forward(50)
    right(45)
    forward(35)
    right(45)
    forward(50)

#Code start

speed(300)
width(5)

H()
spacing()
E()
spacing()
L()
spacing()
L()
spacing()
O()
spacing()
spacing()
W()
spacing()
O()
spacing()
R()
spacing()




