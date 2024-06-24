import turtle as t
import random

t.penup()
t.hideturtle()
t.speed("fastest")
t.colormode(255)
t.setheading(225)
t.forward(300)
t.setheading(0)
colors1 = [(6, 22, 45), (1, 120, 164), (51, 14, 29), (242, 58, 86),
           (171, 17, 40), (251, 107, 125), (0, 83, 119), (252, 204, 193),
           (250, 70, 50), (4, 176, 204), (192, 40, 71), (249, 129, 110),
           (253, 146, 154), (254, 162, 146), (26, 59, 109), (187, 55, 37),
           (252, 11, 14), (97, 209, 200), (251, 191, 204), (49, 205, 218),
           (134, 42, 40), (140, 221, 192), (31, 163, 147), (237, 220, 105),
           (204, 212, 209)]

dots = 100
for dot_no in range(1, dots + 1):
    t.dot(30, random.choice(colors1))
    t.forward(50)
    if dot_no % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen = t.Screen()
t.exitonclick()
