###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
from turtle import Turtle, Screen
import random


SPACE_BETWEEN = 50
SIZE = 20
NUMBER_OF_DOT = 10

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append((color.rgb.r/255, color.rgb.g/255, color.rgb.b/255))


def get_color():
    return random.choice(rgb_colors)


def dot_art(timmy, screen, speed=0):
    if speed in [0, 10, 6, 3, 1]:
        timmy.speed(speed)
    else:
        timmy.speed(0)
    count = 0
    for y in range(-screen.canvheight//2+SIZE//2, screen.canvheight//2, SPACE_BETWEEN+SIZE):
        for x in range(-screen.canvwidth//2+SIZE//2, screen.canvwidth//2, SPACE_BETWEEN+SIZE):
            # print(f"canvas: {screen.canvwidth}")
            # print(f"(x,y)= ({x},{y})")
            count += 1
            timmy.penup()
            timmy.setpos(x, y)
            timmy.dot(SIZE, get_color())
        # print("count:", count)
        # input("")


screen = Screen()
screen.setup(SIZE*NUMBER_OF_DOT + SPACE_BETWEEN*(NUMBER_OF_DOT-1)+50,
             SIZE*NUMBER_OF_DOT + SPACE_BETWEEN*(NUMBER_OF_DOT-1)+50)
screen.screensize(SIZE*(NUMBER_OF_DOT) + SPACE_BETWEEN*(NUMBER_OF_DOT-1),
                  SIZE*(NUMBER_OF_DOT) + SPACE_BETWEEN*(NUMBER_OF_DOT-1))


timmy = Turtle()

timmy.hideturtle()
dot_art(timmy, screen)
screen.exitonclick()
