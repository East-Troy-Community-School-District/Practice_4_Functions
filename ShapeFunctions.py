'''
Shape Functions
2/1/2023
Python I
'''

import random, turtle


def square():
    '''
    Draws a randomly placed square.
    '''
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    t = turtle.Turtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for i in range(0, 4):
        t.forward(100)
        t.left(90)
    t.end_fill()


def rectangle():
  '''
  Draws a randomly placed rectangle.
  '''
  pass


def triangle():
  '''
  Draws a randomly placed triangle.
  '''
  pass


square()
rectangle()
triangle()
