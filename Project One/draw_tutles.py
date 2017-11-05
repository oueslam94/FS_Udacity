#!/usr/bin/env python
import turtle
import time

window = turtle.Screen()
window.bgcolor("black")

brad = turtle.Turtle()
brad.shape("turtle")
brad.color("yellow")
brad.speed(20)

def draw_square(turtle):
    counter = 0
    while counter <4:
        turtle.forward(100)
        turtle.right(90)
        counter+=1
def draw_circle(turtle):
    turtle.circle(100)
def draw_triangle(turtle):
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(180-45)
    turtle.forward(50)

def draw_flower(turtle):
    angle = 0
    while angle <36:
        turtle.forward(100)
        turtle.right(90+10)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        angle = angle + 1
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(300)





#
# draw_square(brad)
# draw_circle(brad)
draw_flower(brad)
time.sleep(10)
