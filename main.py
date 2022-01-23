from turtle import Turtle, Screen, distance
import random
timmy_the_turtle = Turtle()


def change_color(timmy):
    colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
               "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    timmy.color(random.choice(colours))


def random_color(timmy):
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    timmy.pencolor((R/255.0, G/255.0, B/255.0))


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


def random_walk(timmy, distance=30, step=50, speed=0, pensize=5, do_random_color=True):
    """[summary]

    Args:
        timmy ([type]): [description]
        distance (int, optional): [description]. Defaults to 30.
        step (int, optional): [description]. Defaults to 50.
        speed (int, optional): [description]. Defaults to 0.
        pensize (int, optional): [description]. Defaults to 5.
        random_color (bool, optional): [description]. Defaults to True.
    speed:
        “fastest”: 0
        “fast”: 10
        “normal”: 6
        “slow”: 3
        “slowest”: 1
    """

    if speed in ["0,10,6,3,1"]:
        timmy.speed(speed)
    else:
        timmy.speed(0)
    timmy.pensize(pensize)
    angles = [0,  90, 180, 270]
    for _ in range(step):
        angle = random.choice(angles)
        timmy.setheading(angle)
        if(do_random_color):
            random_color(timmy)
        timmy.forward(distance)


timmy_the_turtle.shape("arrow")
timmy_the_turtle.color("coral")
random_walk(timmy_the_turtle, step=200)

screen = Screen()
screen.exitonclick()
