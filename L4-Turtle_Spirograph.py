import turtle as t
import random
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def spirograph(size):
    for _ in range(int(360 / size)):
        t.circle(100)
        t.speed('fastest')
        t.color(random_color())
        t.setheading(t.heading() + size)


spirograph(2)
screen = t.Screen()
screen.exitonclick()
