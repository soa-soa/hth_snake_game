# https://docs.python.org/3/library/turtle.html#
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# creating the game screen
screen = turtle.Screen()
screen.title("The Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
shapes = random.choice(['square', 'triangle', 'circle'])
colors = random.choice(['red', 'green', 'blue'])

food = turtle.Turtle()
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(5,5)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)

def goup():
    if head.direction != "up":
        head.direction = "down"

def godown():
    if head.direction != "down":
        head.direction = "up"

def goright():
    if head.direction != "left":
        head.direction = "right"

def goleft():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y=20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y=20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x=20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x=20)

screen.listen()
screen.onkeypress(goup, "w")
screen.onkeypress(goup, "a")
screen.onkeypress(goup, "s")
screen.onkeypress(goup, "d")

segments = []

# main gameplay
#while True:
#    turtle.update()


turtle.mainloop()
