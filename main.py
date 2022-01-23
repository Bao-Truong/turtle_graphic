from turtle import Turtle, Screen
import random
timmy_the_turtle = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def change_color(timmy):    
    timmy.color(random.choice(colours))


def square(timmy, distance=50):
    for _ in range(4):
        timmy.forward(distance)
        timmy.left(90)


def dashed_line(timmy, distance=10, loop=15):
    for i in range(loop):
        if(i % 2 == 0):
            timmy.pendown()
            timmy.forward(distance)
        else:
            timmy.penup()
            timmy.forward(distance)


def draw_shape(timmy, distance=100, depth=10):
    timmy.speed(1000)
    edge = 3
    while(edge <= depth):
        angle = round(360/edge)
        for i in range(edge):
            timmy.forward(distance)
            timmy.right(angle)
        for i in range(edge):
            timmy.forward(distance)
            timmy.left(angle)
        edge += 1
        change_color(timmy)


def simple_circle(timmy, distance=10, edge=100):
    timmy.speed(1000)
    angle = 360/edge
    for i in range(edge):
        timmy.forward(distance)
        timmy.left(angle)
    edge += 1
    change_color(timmy)



timmy_the_turtle.shape("arrow")
timmy_the_turtle.color("coral")
simple_circle(timmy_the_turtle)

screen = Screen()
screen.exitonclick()
